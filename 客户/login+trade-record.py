# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

class LoginTradeRecord(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://c.test.dongdaodao.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_trade_record(self):
        driver = self.driver
        driver.get(self.base_url + "/user/login")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("18500313747")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("111111")
        driver.find_element_by_id("loginAlertBtn").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"账户管理").click()
        time.sleep(1)

        driver.find_element_by_link_text(u"交易记录").click()
        time.sleep(1)

        driver.find_element_by_link_text(u"查询").click()
        time.sleep(1)

        Select(driver.find_element_by_name("tradeStatus")).select_by_visible_text(u"失败")
        driver.find_element_by_link_text(u"查询").click()
        driver.find_element_by_xpath("(//input[@name='tradeType'])[2]").click()
        driver.find_element_by_link_text(u"查询").click()
        driver.find_element_by_xpath("(//input[@name='tradeType'])[3]").click()
        driver.find_element_by_link_text(u"查询").click()
        driver.find_element_by_xpath("(//input[@name='tradeType'])[4]").click()
        driver.find_element_by_id("selectAll").click()
        driver.find_element_by_id("selectAll").click()
        driver.find_element_by_xpath("(//input[@name='tradeType'])[4]").click()
        driver.find_element_by_link_text(u"查询").click()
        driver.find_element_by_xpath("(//input[@name='tradeType'])[4]").click()
        driver.find_element_by_link_text(u"查询").click()
        driver.find_element_by_id("beginTime").click()
        driver.find_element_by_link_text("20").click()
        driver.find_element_by_id("endTime").click()
        driver.find_element_by_link_text("20").click()
        driver.find_element_by_link_text(u"查询").click()
        Select(driver.find_element_by_name("tradeStatus")).select_by_visible_text(u"成功")
        driver.find_element_by_link_text(u"查询").click()
    
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
