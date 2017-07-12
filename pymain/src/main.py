# -*- coding: utf-8 -*-

'main'

from pac import hello
import sub


def main():
    'main#main()'
    return hello.hello() + sub.sub()


if __name__ == '__main__':
    print(main())
