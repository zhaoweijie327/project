from selenium.webdriver.common.by import By

'''
管理元素属性值
'''
class FindElement:

    # -------------------主页面-------------------
    shaohou_gengxin = (By.ID,'com.bjcsxq.chat.carfriend:id/bt_no') # 定位稍后更新
    my_de = (By.ID,'com.bjcsxq.chat.carfriend:id/tv_home_mine')    # 定位我的

    # -------------------我的 页面-------------------
    login_zhuce = (By.ID,'com.bjcsxq.chat.carfriend:id/mine_username_tv')  # 定位登陆/注册

    # -------------------登陆页面-------------------
    back = (By.ID,'com.bjcsxq.chat.carfriend: id/title_back')  # 定位返回键
    login_user = (By.ID,'com.bjcsxq.chat.carfriend:id/login_phone_et') # 定位用户名输入框
    login_pwd = (By.ID,'com.bjcsxq.chat.carfriend:id/login_pwd_et')    # 定位密码输入框
    login_button = (By.ID,'com.bjcsxq.chat.carfriend:id/login_btn')    # 定位登陆按钮