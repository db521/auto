# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LoginConfirmOrder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #verify环境
        self.base_url = "http://cp.verify.idaodao.net/"
        #测试环境
        #self.base_url = "http://k.test.dongdaodao.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_confirm_order(self):
        #登录
        driver = self.driver
        driver.get(self.base_url + "/user/auth/login")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("13810770500")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("loginBtn").click()
        #火狐的angularJS兼容性还有点问题，弹窗需要点一下
        self.assertEqual(
            "DataTables warning: table id=dt_basic - Cannot reinitialise DataTable. For more information about this error, please see http://datatables.net/tn/3",
            self.close_alert_and_get_its_text())

        #确认订单
        driver.find_element_by_css_selector("td.green").click()
        driver.find_element_by_id("payForfor").click()
        driver.find_element_by_link_text("13").click()
        driver.find_element_by_css_selector("i.fa.fa-plus").click()
        Select(driver.find_element_by_id("businessCategory")).select_by_visible_text(u"品牌设计")
        driver.find_element_by_id("priceInput").send_keys("1000")
        driver.find_element_by_id("process1").click()
        driver.find_element_by_css_selector("#businessCategory > option[value=\"2\"]").click()
        Select(driver.find_element_by_id("requirementCategory")).select_by_visible_text("logo")
        driver.find_element_by_id("evilButton").click()
        driver.find_element_by_id("process1").click()
        driver.find_element_by_link_text("19").click()
        driver.find_element_by_id("process2").click()
        driver.find_element_by_link_text("20").click()
        driver.find_element_by_id("process3").click()
        driver.find_element_by_link_text("21").click()
        driver.find_element_by_id("process4").click()
        driver.find_element_by_link_text("22").click()
        driver.find_element_by_id("process5").click()
        driver.find_element_by_link_text("23").click()
        driver.find_element_by_id("process6").click()
        driver.find_element_by_link_text("24").click()
        driver.find_element_by_id("reTextarea").clear()
        driver.find_element_by_id("reTextarea").send_keys(u"需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述需求描述")
        driver.find_element_by_id("commitOrderBtn1").click()
        driver.find_element_by_id("commitOrderBtn2").click()
        driver.find_element_by_id("partBTn1").click()
        driver.find_element_by_id("nav_1_1").click()
    
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
        print "确认订单"
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
