#!/usr/bin/python
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import easygui as g
import tkinter
import tkthread
from PIL import Image
import threading
import os
import json

#易班
g.msgbox("请在网页中登录自己的百度账号")
url = 'https://baidu.com'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(20)
g.msgbox("输入完成后请点击确认，等待程序存储cookie")
cookies = driver.get_cookies()
with open("c:\cookies.txt", "w") as fp:
    json.dump(cookies, fp)
g.msgbox("cookie已存储，可以开始运行")