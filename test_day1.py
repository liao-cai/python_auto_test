def test_addition():
    """测试加法功能"""
    assert 1 + 1 == 2
    print("加法测试通过！")

def test_string():
    """测试字符串处理"""
    assert "hello".upper() == "HELLO"
    print("字符串测试通过！")

if __name__ == "__main__":
    test_addition()
    test_string()
    print("所有测试通过！环境配置成功！")