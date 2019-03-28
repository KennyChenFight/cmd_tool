import click


# click接下來的參數預設為str，所以須轉型
@click.command()
@click.option('-a', '--a', help='參數a')
@click.option('-b', '--b', help='參數b')
def add(a, b):
    click.echo(int(a) + int(b))


if __name__ == '__main__':
    result = add()
    print(result)