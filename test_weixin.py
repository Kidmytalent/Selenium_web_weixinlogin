# -*- coding: utf-8 -*-
# @Author： Kid
# @FileName: test_weixin.py
import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo0():
    def setup_method(self, method):
        # option = Options()  # 复用浏览器三个步骤
        # option.debugger_address = 'localhost:9222'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        # 加隐式等待， ******最好是在实例化driver之后立刻去设置，
        # 因为会存在于driver整个生命当中，全局性的等待，直到self.driver结束
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_cookie(self):

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
         # get_cookies()获取当前页面的cookies

        # cookies = self.driver.get_cookies()  # 这里不是 get_cookie()
        # print(cookies)  # 拿到后的cookies,带有登录信息的
        # # 现在用cookie模拟，先打开index页面,这时候需要登录
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850415892339'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'oX8wFwR7qAm9JYB7v3FeOodVOdoeHS8Fp2MBH8cQDHJmubYTyrnrLCA2_8ALqAqGKO26P2bdSN3I2dXByMRWwK8qxCIUp-9TWFmBG8DEu4K3_RqA9Qe8q_gomg5WNX7gQnNIw6KD0tyQxnNOsvwIp9xeSnFBYPPEPZBIf-XlBsua_GlfIBd6LVvEHj6xpEtl8PAZZEg8ocnPTM792wa5QcmkWH3n0Cvs_LTg33qhN4CKlTH-Lisy0PmrLMC7g0jXU0o8LwR7sj1Pt2GRVJY2Mw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850415892339'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325112426029'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645853138, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614317139'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'sites'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a4410610'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'giqYy9KDQVpw3Df734Tx5VHpSa6ulcTAAimd7xTcR4AySqrI0YcEtuQcHVY9MsyQ'}, {'domain': 'work.weixin.qq.com', 'expiry': 1614348673, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '4sq3pvh'}, {'domain': '.qq.com', 'expiry': 1614410659, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1437006777.1614317139'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '3951499431402935'}, {'domain': '.qq.com', 'expiry': 1677396259, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1728778928.1614317139'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645853137, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1616916262, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        for cookie in cookies:  # 列表里面多个字典，用for遍历
            if 'expiry' in cookie.keys():   # expiry时间戳，浮点数
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)  # 加入cookie，复用浏览器可以不要了
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def test_importcontact(self):

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850415892339'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'oX8wFwR7qAm9JYB7v3FeOodVOdoeHS8Fp2MBH8cQDHJmubYTyrnrLCA2_8ALqAqGKO26P2bdSN3I2dXByMRWwK8qxCIUp-9TWFmBG8DEu4K3_RqA9Qe8q_gomg5WNX7gQnNIw6KD0tyQxnNOsvwIp9xeSnFBYPPEPZBIf-XlBsua_GlfIBd6LVvEHj6xpEtl8PAZZEg8ocnPTM792wa5QcmkWH3n0Cvs_LTg33qhN4CKlTH-Lisy0PmrLMC7g0jXU0o8LwR7sj1Pt2GRVJY2Mw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850415892339'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325112426029'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645853138, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614317139'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'sites'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a4410610'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'giqYy9KDQVpw3Df734Tx5VHpSa6ulcTAAimd7xTcR4AySqrI0YcEtuQcHVY9MsyQ'}, {'domain': 'work.weixin.qq.com', 'expiry': 1614348673, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '4sq3pvh'}, {'domain': '.qq.com', 'expiry': 1614410659, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1437006777.1614317139'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '3951499431402935'}, {'domain': '.qq.com', 'expiry': 1677396259, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1728778928.1614317139'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645853137, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1616916262, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys("D:\web_weixin_Login_contact/mydata.xls")
        assert "mydata.xls" == self.driver.find_element(By.ID, "upload_file_name").text
        sleep(5)


    def test_shelve(self):
        # shelve python 内置的模块，相当于小型 数据库
        db = shelve.open('./mydbs/cookies')
        # db['cookie'] = cookies  # 定义了一个数据库的key, 把整个cookies 放到key里面
        # db.close()  # 已经生成存好
        cookies = db['cookie']  # 取出来


