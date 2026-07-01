#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/7/1 12:41
# @Author  : liuronggui
# @File    : test_main.py
from main import add

def test_add():
    assert add(1, 2) == 3
    assert add(5, 5) == 10