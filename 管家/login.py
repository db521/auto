# -*- coding: utf-8 -*-
import time
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class LoginConfirmOrder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://k.idaodao.net"
        #verify环境
        # self.base_url = "http://k.verify.idaodao.net/"
        #测试环境
        # self.base_url = "http://k.test.dongdaodao.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_confirm_order(self):
        #登录
        driver = self.driver
        driver.get(self.base_url + "/user/auth/login")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("18911888540")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("111111")
        driver.find_element_by_id("loginBtn").click()
        #火狐的angularJS兼容性还有点问题，弹窗需要点一下
        self.assertEqual(
            "DataTables warning: table id=dt_basic - Cannot reinitialise DataTable. For more information about this error, please see http://datatables.net/tn/3",
            self.close_alert_and_get_its_text())
        #检查页面内容
        driver.find_element_by_link_text(u"订单管理").click()
        driver.find_element_by_link_text(u"未完成订单").click()
        driver.find_element_by_link_text(u"已完成订单").click()
        driver.find_element_by_xpath("//ul[@id ='navModuleList']/li[3]/a/span").click()
        driver.find_element_by_link_text(u"银行卡管理").click()
        driver.find_element_by_link_text(u"提现").click()
        driver.find_element_by_link_text(u"提现明细").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"我的资料").click()
        driver.find_element_by_link_text(u"账号管理").click()
        driver.find_element_by_link_text(u"简历管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"我的设置").click()
        driver.find_element_by_link_text(u"接单设置").click()
        driver.find_element_by_link_text(u"意见反馈").click()
        driver.find_element_by_link_text(u"帮助中心").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        print "登录成功"
        # self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
