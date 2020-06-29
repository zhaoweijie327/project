from Base.base import Base
from Page.pageElements import PageElements


class PersonPage(Base):

    def __init__(self):
        super().__init__()

    def click_login_sign_btn(self):
        """点击登录注册按钮"""
        self.click_ele(PageElements.person_login_sign_btn_xpath)
