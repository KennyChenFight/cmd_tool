import argparse


# argparse接下來的參數預設為str，所以須轉型
def add(a, b):
    return int(a) + int(b)


if __name__ == '__main__':
    # 初始化解析器
    parser = argparse.ArgumentParser()

    # 定義參數
    parser.add_argument('-a', '--a', help='參數a')
    parser.add_argument('-b', '--b', help='參數b')

    # 解析
    args = parser.parse_args()
    result = add(args.a, args.b)
    print(result)