from selenium.webdriver.support.wait import WebDriverWait

from base.driver import Driver

'''
封装显示等待、元素定位方法、操作方法
'''


class Base:

    # 初始化
    def __init__(self):
        self.driver = Driver().driver_open()

    def search_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CLASS_NAME,属性值)
        :param timeout: 搜索超时时间
        :param poll_frequency: 搜索间隔
        :return: 返回定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll_frequency=1.0):
        """
        定位一组元素
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CLASS_NAME,属性值)
        :param timeout: 搜索超时时间
        :param poll_frequency: 搜索间隔
        :return: 返回定位对象列表
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        点击元素
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CLASS_NAME,属性值)
        :param timeout: 搜索超时时间
        :param poll_frequency: 搜索间隔
        :return:
        """
        self.search_ele(loc, timeout, poll_frequency).click()

    def send_ele(self, loc, text, timeout=5, poll_frequency=1.0):
        """
        输入文本内容
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CLASS_NAME,属性值)
        :param text: 文本内容
        :param timeout: 搜索超时时间
        :param poll_frequency: 搜索间隔
        :return:
        """
        # 定位
        input_text = self.search_ele(loc, timeout, poll_frequency)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)