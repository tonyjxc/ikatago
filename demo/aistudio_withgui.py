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
import string
import sys

def fun1():
    url = 'https://aistudio.baidu.com/aistudio/index'
    #无界面登录部分
    # chrome_opt = Options()      # 创建参数设置对象.
    # chrome_opt.add_argument('--headless')   # 无界面化.
    # chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.

    # driver = webdriver.Chrome(chrome_options=chrome_opt)
    # driver.get(url)
    #界面
    driver = webdriver.Chrome()
    driver.set_window_size(1300, 1000)
    driver.get(url)

    #login
    # 设置cookies前必须访问一次
    with open(r'c:\cookies.txt', "r") as fp:
        cookies = json.load(fp)
        for cookie in cookies:
            # cookie.pop('domain')  # 如果报domain无效的错误
            driver.add_cookie(cookie)
    driver.get(url)

    #项目
    driver.find_elements_by_class_name('studio-container-item')[0].click()
    time.sleep(1)
    #我的项目
    driver.find_elements_by_class_name('ant-tabs-tab')[1].click()
    time.sleep(1)
    
    #启动
    urls = driver.find_elements_by_class_name('item-content-link')
    url = urls[10].get_attribute("href")
    driver.get(url)
    url=(os.path.abspath((__file__)  )+"\..\\js\\aistudio1.js")
    f = open(url, encoding='UTF-8')
    js=f.read()
    f.close()
    driver.execute_script(js)
    g.msgbox("开始等待GPU分配大约需要20s")

    while 1:
        now_url = driver.current_url
        urlpp = ["https://aistudio.baidu.com/bdvgpu/user/" , "https://aistudio.baidu.com/bdvgpu32g/user/"] 
        if ((urlpp[0] in now_url )or (urlpp[1] in now_url)) :
            g.msgbox("获取到GPU，请等待项目运行")
            url=(os.path.abspath((__file__)  )+"\..\\js\\aistudio2.js")
            f = open(url, encoding='UTF-8')
            js=f.read()
            f.close()
            driver.execute_script(js)
            break
        time.sleep(3)
    g.msgbox("加载完毕，请打开围棋软件进行连接")
          

if __name__ == "__main__":
    g.msgbox("欢迎使用请稍后")
    #main()
    fun1()
    g.msgbox("当您不打算使用ikatago时点击确认以退出")