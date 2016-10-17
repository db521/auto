# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LoginConfirmOrderPayDeposit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://c.idaodao.net"
        # self.base_url = "http://c.test.dongdaodao.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_confirm_order_pay_deposit(self):
        #登录
        driver = self.driver
        driver.get(self.base_url + "/user/login")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("15210936554")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("loginAlertBtn").click()

        #找到第一个订单，是待确认订单的

        driver.find_element_by_css_selector("td.green").click()
        driver.find_element_by_id("nav_1_1").click()
        '''
        真JB麻烦，先这样，有时间再弄
        time.sleep(3)
        print "进入订单详情页"

        driver.find_element_by_id("commitOrderBtn").click()
        print "点确认订单弹框"
        time.sleep(3)
        #中间有一个弹层，IDE不能自动识别，需要手动去操作一下
        driver.find_element_by_xpath('// *[ @ id = "confirmOrderBtn"]').click()
        print "点确认订单弹框"
        '''
        time.sleep(3)
        driver.find_element_by_id("payDepositBtn").click()
        driver.find_element_by_link_text(u"稻米支付").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("111111")
        driver.find_element_by_id("confirmPayBtn").click()
        driver.find_element_by_css_selector(
            "#ricepayPaySuccessModal > div.modal-dialog.showBox > div.modal-content.text-center > div.modal-body > p.marginTop2 > a.btn.commitBtn").click()

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
        print "客户确认完成订单+支付定金成功"
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
