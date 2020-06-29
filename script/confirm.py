from base.ition_page import Page

# 首页-稍后更新+点击我的
Page.get_home().click_my_btn()

# 个人中心 -登录/注册
Page.get_person().click_login_sign_btn()

# 登录页面 -登录
Page.get_login().login("15015754120", "kg83200477")

# 登录页面 -登录确认
Page.get_login().login_acc_btn()

# 个人中心 -获取用户名
print("用户名:", Page.get_person().get_user_name())

# 个人中心 -点击设置
Page.get_person().click_setting_btn()

# 设置页面 -退出 -向下滑动页面
Page.get_setting().logout()
