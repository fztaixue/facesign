# -*- coding: utf-8 -*-
# @File  : shutdownjava.py
# @Author: Feng
# @Date  : 2019/1/23
# @Desc  :

import re
import codecs
import locale
import subprocess

ps = subprocess.Popen('netstat -nltup', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

while True:
    data = ps.stdout.readline()
    if data == b'':
        break
    data = data.decode(codecs.lookup(locale.getpreferredencoding()).name)
    search = re.search(r'(\d*)?/python', data)
    print(search)
    if search is not None:
        pid = search[1]
        print(pid)
        subprocess.Popen('kill -9 ' + str(pid), stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)