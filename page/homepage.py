from selenium.common.exceptions import TimeoutException

from base.base_driver import Base
from base.findelement import PageElements

'''定位元素并操作'''

class HomePage(Base):

    # 初始化
    def __init__(self):
        super().__init__()

    # 定位并操作
    def click_my_btn(self):
        """点击我的"""
        try:
            # 点击稍后更新
            self.click_ele(PageElements.home_update_later_xpath)
        except TimeoutException:
            print("当前版本app没有更新提示框")
        # 点击我的
        self.click_ele(PageElements.home_my_btn_id)