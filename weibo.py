# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:19:06 2017

@author: lx
"""

# 安装
# pip install selenium
import time
from selenium import webdriver

browser = webdriver.Firefox() # 使用火狐浏览器
browser.get('https://weibo.com') # 访问微博首页

time.sleep(10)

username = '' # 用户名
password = '' # 用户密码

username_input = browser.find_element_by_id('loginname') # 获取用户名所在输入
password_input = browser.find_element_by_name('password') # 获取密码输入框

username_input.clear() # 清空用户名输入框
username_input.send_keys(username) # 填写用户名
password_input.clear()
password_input.send_keys(password)

# 得到登录按钮
login_btn = browser.find_element_by_css_selector('.info_list.login_btn>a')
login_btn.click() # 执行登录

time.sleep(10)

weibo_tags = browser.find_elements_by_class_name('WB_detail') # 获取微博标签列表

contents = {}

for weibo_tag in weibo_tags:
    # 获取名字
    name = weibo_tag.find_element_by_css_selector('div.WB_info>a').text
    text = weibo_tag.find_element_by_css_selector('div.WB_text').text
    contents.update({name:text})

print(contents)

