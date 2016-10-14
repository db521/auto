# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CustomerLoginTopUnauthDataManagement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://c.verify.idaodao.net"
        # self.base_url = "http://c.test.dongdaodao.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_customer_login_top_unauth_data_management(self):
        #登录PC
        driver = self.driver
        driver.get(self.base_url + "/user/login")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("17561646509")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("111111")
        driver.find_element_by_id("loginAlertBtn").click()
        #进入资料管理页
        time.sleep(3)
        driver.find_element_by_link_text(u"点击快速进行完善").click()
        driver.find_element_by_id("nav_3_2").click()
        driver.find_element_by_id("realName").clear()
        driver.find_element_by_id("realName").send_keys(u"阿斯顿")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("12341234@1212.com")
        Select(driver.find_element_by_id("provId")).select_by_visible_text(u"北京")
        Select(driver.find_element_by_id("areaId")).select_by_visible_text(u"丰台区")
        time.sleep(3)
        driver.find_element_by_id("userInfoSave").click()
        time.sleep(1)
        #图片上传的有时间再弄
        # driver.find_element_by_id("avatarImg").click()
        # driver.find_element_by_css_selector("a.upload-img > label").click()
        # driver.find_element_by_id("upload-file").clear()
        # driver.find_element_by_id("upload-file").send_keys("C:\\Users\\admin.DEMO-20150812LX\\Desktop\\QQ20160902103150.jpg")
        # driver.find_element_by_id("imgSave").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(u"的非官方的股份")
        Select(driver.find_element_by_id("industryId")).select_by_visible_text(u"建筑业")
        driver.find_element_by_name("department").clear()
        driver.find_element_by_name("department").send_keys(u"是掉发的发地方")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(u"东方不败v")
        driver.find_element_by_name("years").clear()
        driver.find_element_by_name("years").send_keys("34")
        Select(driver.find_element_by_id("registeredCapitalId")).select_by_visible_text(u"2000-5000万")
        Select(driver.find_element_by_id("enterpriseTypeId")).select_by_visible_text(u"省级级别及主版上市企业")
        Select(driver.find_element_by_id("staffTotalId")).select_by_visible_text(u"100-299人")
        Select(driver.find_element_by_id("incomeId")).select_by_visible_text(u"5000-10000万")
        driver.find_element_by_id("verifyCompanyInfo").click()
    
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
        print "资料已经添加"
        # self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
