from base.base_driver import Base
from base.findelement import FindElement

'''定位元素并操作'''

class HomePage(Base):

    # 初始化
    def __init__(self):
        super().__init__()

    # 定位并操作
    def find_caozuo_fangfa(self,username,pwd):
        # 点击稍后更新
        self.find_click(FindElement.shaohou_gengxin)
        # 点击右下角我的
        self.find_click(FindElement.my_de)
        # 跳转到我的页面点击登陆/注册
        self.find_click(FindElement.login_zhuce)
        # 跳转到登陆页面输入用户名
        self.find_send_key(FindElement.login_user,username)
        # 跳转到登陆页面输入密码
        self.find_send_key(FindElement.login_pwd,pwd)
        # 跳转到登陆页面点击登陆按钮
        self.find_click(FindElement.login_button)