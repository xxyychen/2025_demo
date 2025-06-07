# -*- coding = utf-8 -*-
# @Time : 2025/4/30 22:40
# @Software: PyCharm

def main():
    '''
    url编码

    '''
    # url编码
    from urllib.parse import quote, unquote

    # 编码
    keyword = "我的"
    keyword_encoded = quote(keyword)
    print("编码后:", keyword_encoded)  # %E6%88%91%E7%9A%84

    # 解码
    decoded = unquote(keyword_encoded)
    print("解码后:", decoded)  # 我的

    # 转换为 bytes类型
    print('Python'.encode().decode())

    print('我的'.encode().decode())
    print('我的'.encode())


if __name__ == "__main__":
    main()
