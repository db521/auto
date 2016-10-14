# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://cp.idaodao.net"
        #self.base_url = "http://cp.verify.idaodao.net"
        #self.base_url = "http://cp.test.dongdaodao.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/user/login")
        driver.find_element_by_id("phone").clear()
        #1551111111
        driver.find_element_by_id("phone").send_keys("18561175548")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("111111")
        driver.find_element_by_id("loginBtn").click()
        driver.find_element_by_link_text(u"订单管理").click()
        driver.find_element_by_link_text(u"未完成订单").click()
        driver.find_element_by_link_text(u"已完成订单").click()
        driver.find_element_by_xpath("//ul[@id='navModuleList']/li[3]/a/span").click()
        driver.find_element_by_link_text(u"银行卡管理").click()
        driver.find_element_by_link_text(u"提现").click()
        driver.find_element_by_link_text(u"提现明细").click()
        driver.find_element_by_xpath("//ul[@id='navModuleList']/li[4]/a/span").click()
        driver.find_element_by_link_text(u"帐号管理").click()
        driver.find_element_by_link_text(u"资料管理").click()
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
