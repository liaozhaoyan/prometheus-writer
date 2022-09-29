# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     slsTest
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
from prometheus.Writer import CslsWriter


def test():
    with open("auth.txt", 'r') as f:
        lines = f.readlines()
        endpoint = lines[0].strip()
        project = lines[1].strip()
        store = lines[2].strip()
        auth = (lines[3].strip(), lines[4].strip())

    w = CslsWriter(endpoint, project, store, auth)
    while True:
        lines = (
            ("random_test", {"hello": "world"}, random.uniform(10, 20)),
            ("random_test", {"hello": "world2"}, random.uniform(10, 20)),
        )
        w.writes(lines)
        time.sleep(15)


if __name__ == "__main__":
    test()
    pass
