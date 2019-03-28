import sys


# sys.argv接下來的參數預設為str，所以須轉型
def add(a, b):
    return int(a) + int(b)


if __name__ == '__main__':
    result = add(sys.argv[1], sys.argv[2])
    print(result)
