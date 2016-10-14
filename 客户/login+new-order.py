# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CustomerLoginNewOrder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://c.verify.idaodao.net"
        # self.base_url = "http://c.test.dongdaodao.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_customer_login_new_order(self):
        driver = self.driver
        driver.get(self.base_url + "/user/login")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("17561646509")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("111111")
        driver.find_element_by_id("loginAlertBtn").click()
        driver.find_element_by_css_selector("a.releaseBtn1").click()
        print "登录成功"
        time.sleep(3)
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"测试发布新需求")
        print "测试发布新需求"
        driver.find_element_by_id("budget").clear()
        driver.find_element_by_id("budget").send_keys("202312")
        print "202312"
        time.sleep(3)
        driver.find_element_by_id("expectedTime").click()
        driver.find_element_by_link_text("20").click()
        print "20"
        driver.find_element_by_id("2").click()
        driver.find_element_by_id("description").clear()
        driver.find_element_by_id("description").send_keys(u"测试发布新需求测试发布新需求测试发布新需求测试发布新需求测试发布新需求测试发布新需求测试发布新需求测试发布新需求测试发布新需求测试发布新需求")
        #上传图片，脚本里面暂时不要
        # driver.find_element_by_name("file").click()
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]

        # 认证通过使用demandSuccessBtn
        # driver.find_element_by_id("demandSuccessBtn").click()
        #没有认证过的使用下面的releaseBtn和dataSuccessBtn

        driver.find_element_by_id("releaseBtn").click()
        time.sleep(10)
        driver.find_element_by_id("dataSuccessBtn").click()

    
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
        print "发布需求完成"
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
