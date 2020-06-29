import os

import yaml
from appium import webdriver
'''
封装driver对象
app启动参数
关闭app驱动
数据传输

'''



class Driver:

    __driver = None

    # 启动App
    @classmethod
    def driver_open(cls):
        if cls.__driver is None:
            data = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.bjcsxq.chat.carfriend',
                'appActivity': '.module_main.activity.MainActivity'
            }
            cls.__driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',data)
            return cls.__driver
        else:
            return cls.__driver

    # 关闭app驱动
    @classmethod
    def driver_close(cls):
        if cls.__driver:
            cls.driver_open().quit()
            cls.__driver = None

    # 数据驱动
    @classmethod
    def data_yaml(cls,filepath):
        data_list = []
        with open('./data' + os.sep + filepath,'r',encoding='utf-8') as file :
            data = yaml.safe_load(file)
            for i in data.values():
                data_list.append(list(i.values()))
        return data_list