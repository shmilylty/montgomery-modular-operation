#!/usr/bin/env python
# coding=utf-8
# author:admin[@hackfun.org]
# license:GPL v3
# blog:hackfun.org
# x = a^d n n
def montgomery(a, d, n):
    x = 1
    while d:
        if (d & 1):
            x = (x * a) % n
        d >>= 1  
        a = (a * a) % n
    return x