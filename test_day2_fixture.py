import pytest

# fixture: 测试前的准备工作（类似单片机初始化）
@pytest.fixture
def serial_connection():
    """模拟串口连接"""
    print("\n[SETUP] 正在连接串口...")
    # 这里假装连接成功，返回一个模拟对象
    connection = {"port": "COM3", "baudrate": 115200, "status": "connected"}
    yield connection  # yield 返回给测试函数用
    # yield 后面的代码是清理工作（类似反初始化）
    print("[TEARDOWN] 关闭串口连接")

# 使用 fixture 的测试函数
def test_read_temperature(serial_connection):
    """测试读取温度传感器"""
    # 直接使用 fixture 提供的数据
    assert serial_connection["status"] == "connected"
    assert serial_connection["baudrate"] == 115200
    print(f"通过 {serial_connection['port']} 读取温度: 25°C")

def test_read_humidity(serial_connection):
    """测试读取湿度传感器"""
    assert serial_connection["status"] == "connected"
    print(f"通过 {serial_connection['port']} 读取湿度: 60%")

# 参数化测试：一次测试多组数据（类似循环测试多个寄存器）
@pytest.mark.parametrize("voltage,expected", [
    (3.3, True),   # 正常电压
    (3.0, True),   # 边界值
    (5.0, False),  # 过压（应该报错）
])
def test_voltage_check(voltage, expected):
    """测试电压检测（模拟硬件保护机制）"""
    result = voltage < 3.6  # 假设 3.6V 是最大允许电压
    assert result == expected
    print(f"电压 {voltage}V 检测 {'通过' if result else '失败'}")