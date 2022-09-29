# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     base.py
   Description :
   Author :       liaozhaoyan
   date：          2022/9/28
-------------------------------------------------
   Change Activity:
                   2022/9/28:
-------------------------------------------------
"""
__author__ = 'liaozhaoyan'

import time
import random
from prometheus.Writer import Cwriter


def test():
    w = Cwriter("http://192.168.22.7:9090/api/v1/write")
    while True:
        w.write("random_test", {"hello": "world"}, random.uniform(10, 20))
        time.sleep(15)


if __name__ == "__main__":
    test()
    pass
