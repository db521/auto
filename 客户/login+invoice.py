# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LoginInvoice(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://c.test.dongdaodao.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_invoice(self):
        driver = self.driver
        driver.get(self.base_url + "/user/login")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("18500594347")
        driver.find_element_by_id("password").click()
        # print   driver.find_element_by_css_selector("css=label.class=error").text
        # print   driver.find_element_by_tag_name("label").text
        try:
            # self.assertEqual(u"手机号不正确，请重新输入",driver.find_element_by_xpath("//label[@class='error']").text)
            self.assertEqual(u"手机号不正确，请重新输入", driver.find_element_by_tag_name("label").text)
        except AssertionError as e:
            print u"找不到这个错误提示"

        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("111111")
        driver.find_element_by_id("loginAlertBtn").click()
        driver.find_element_by_link_text(u"账户管理").click()
        driver.find_element_by_link_text(u"发票管理").click()
        driver.find_element_by_id("invoiceValue").clear()
        driver.find_element_by_id("invoiceValue").send_keys("2000")
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(u"我是发票抬头")
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"我是收件人")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys(u"18500313741")

        Select(driver.find_element_by_id("provId")).select_by_visible_text(u"辽宁")
        Select(driver.find_element_by_id("areaId")).select_by_visible_text(u"丹东")
        driver.find_element_by_id("address").clear()
        driver.find_element_by_id("address").send_keys(u"我是详细地址")
        driver.find_element_by_id("invoiceManageBtn").click()
        driver.find_element_by_id("invoiceBtn").click()
    
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
