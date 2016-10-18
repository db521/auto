# -*- coding: utf-8 -*-
import random

from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

class Signup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        # self.base_url = "http://cp.idaodao.net"
        # self.base_url = "http://cp.verify.idaodao.net"
        self.base_url = "http://cp.test.dongdaodao.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_signup(self):
        driver = self.driver
        driver.get(self.base_url + "/user/login")
        driver.find_element_by_link_text(u"注册").click()
        driver.find_element_by_id("phone").clear()
        #金秋手机号
        driver.find_element_by_id("phone").send_keys("15010687780")
        driver.find_element_by_link_text(u"获取验证码").click()

        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("111111")
        driver.find_element_by_id("confirmPassword").clear()
        driver.find_element_by_id("confirmPassword").send_keys("111111")
        driver.find_element_by_id("agreement").click()



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
        print "供应商-个人-注册-短信验证码OK"
        # self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
