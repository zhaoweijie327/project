from selenium.webdriver.support.wait import WebDriverWait

from base.driver import Driver

'''
封装显示等待、元素定位方法、操作方法
'''


class Base:

    # 初始化
    def __init__(self):
        self.driver = Driver().driver_open()

    # 封装显示等待定位单个元素
    def find_ele_wait(self,loc,time_wait=10,time_sousuo=1.0):
        '''
        封装显示等待定位单个元素
        :param loc: 定位方式+定位元素
        :param time_wait: 等待时间
        :param time_sousuo: 搜索间隔时间
        :return:
        '''
        return WebDriverWait(self.driver,time_wait,time_sousuo).until(lambda x : x.fin_element(*loc))

    # 封装显示等待定位单个元素
    def find_eles_wait(self,loc,time_wait=10,time_sousuo=1.0):
        '''
        封装显示等待定位一组元素
        :param loc: 定位方式+定位元素
        :param time_wait: 等待时间
        :param time_sousuo: 搜索间隔时间
        :return:
        '''
        return WebDriverWait(self.driver,time_wait,time_sousuo).until(lambda x : x.fin_elements(*loc))

    # 封装点击操作
    def find_click(self,loc):
        '''
        封装点击操作
        :param loc:  定位元素
        :return:
        '''
        self.find_ele_wait(loc).click()

    # 封装输入操作
    def find_send_key(self,loc,text):
        '''
        封装输入操作
        :param loc: 定位元素
        :param text: 输入的内容
        :return:
        '''
        send_key = self.find_ele_wait(loc)
        send_key.clear()
        send_key.send_keys(text)

    # 封装获取信息
    def find_text(self,element):
        '''
        封装获取信息
        :param element: 获取的元素的信息
        :return:
        '''
        return element.text