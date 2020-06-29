from base.base_driver import Base
from base.findelement import PageElements


class SettingPage(Base):

    def __init__(self):
        super().__init__()

    def logout(self, tag=1):
        """
        退出操作
        :param tag: 1 确认退出 2 取消退出
        :return:
        """
        # 点击退出
        self.click_ele(PageElements.setting_logout_btn_id)
        if tag == 1:
            # 点击确认退出
            self.click_ele(PageElements.setting_logout_acc_btn_id)
            # 向下滑动
            self.swipe_screen(2)
        if tag == 2:
            # 点击取消退出
            self.click_ele(PageElements.setting_logout_dis_btn_id)
