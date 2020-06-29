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

    def swipe_screen(self, tag=1):
        """
        滑动屏幕
        :param tag: 1:向上 2:向下 3:向左 4: 向右
        :return:
        """
        # 分辨率
        size = self.driver.get_window_size()
        # 宽
        width = size.get("width")
        # 高
        height = size.get("height")
        time.sleep(1)
        # 滑动 上下 高80 -高20 宽50   左右 宽80 -宽20 高50
        if tag == 1:
            # 向上滑动
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)
        if tag == 2:
            # 向下滑动
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 2000)
        if tag == 3:
            # 向左滑动
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 2000)
        if tag == 4:
            # 向右滑动
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 2000)
