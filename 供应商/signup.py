# -*- coding: utf-8 -*-
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Signup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://cp.idaodao.net"
        # self.base_url = "http://cp.verify.idaodao.net"
        # self.base_url = "http://cp.test.dongdaodao.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_signup(self):
        driver = self.driver
        driver.get(self.base_url + "/user/login")
        driver.find_element_by_link_text(u"注册").click()
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("185616"+bytes(random.randint(10000, 99999)))
        driver.find_element_by_id("phoneCode").clear()
        driver.find_element_by_id("phoneCode").send_keys("1234")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("111111")
        driver.find_element_by_id("confirmPassword").clear()
        driver.find_element_by_id("confirmPassword").send_keys("111111")
        driver.find_element_by_id("agreement").click()

        #加入暂停10秒钟,手动输入验证码
        time.sleep(20)


        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(u"你说啥")
        driver.find_element_by_id("yearsWorking").clear()
        driver.find_element_by_id("yearsWorking").send_keys("2")
        driver.find_element_by_name("gender").click()
        driver.find_element_by_id("yearsWorking").clear()
        driver.find_element_by_id("yearsWorking").send_keys("23")
        Select(driver.find_element_by_id("provId")).select_by_visible_text(u"北京")
        Select(driver.find_element_by_id("areaId")).select_by_visible_text(u"顺义区")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(u"按时大大飒飒大师的萨达")
        driver.find_element_by_name("idCardNo").clear()
        driver.find_element_by_name("idCardNo").send_keys("371421198801210038")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("1212@123123.com")

        # 目前没时间，先手动上传
        # 测试上传，找到隐藏的元素
        # js = 'document.querySelectorAll("idCardImgA")[0].style.type="file";'

        # js1 = 'document.getElementById("idCardImgA")[0].style.id="visible";'
        # time.sleep(5)
        # driver.execute_script(js1)
        # js2 = 'document.getElementById("idCardImgA")[0].style.id="visible";'
        # driver.execute_script(js2)
        #
        # print  driver.execute_script(js2)
        # driver.find_element_by_name('idCardImgA').send_keys(r"C:\Users\admin.DEMO-20150812LX\Desktop\QQ20160902103150.jpg")


        #------------------------------------

        #driver.find_element_by_name("idCardImgA").send_keys(r"C:\Users\admin.DEMO-20150812LX\Desktop\QQ20160902103150.jpg")

        #加入暂停10秒钟,手动输入验证码

        time.sleep(10)
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        #driver.find_element_by_name("file").click()
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]

        driver.find_element_by_link_text(u"添加教育经历").click()
        driver.find_element_by_id("school").clear()
        driver.find_element_by_id("school").send_keys(u"地方水电费地方")
        Select(driver.find_element_by_id("degree")).select_by_visible_text(u"高中")
        driver.find_element_by_id("major").clear()
        driver.find_element_by_id("major").send_keys(u"水电费v发送到高")
        driver.find_element_by_id("eduTime2").click()
        driver.find_element_by_link_text("19").click()
        driver.find_element_by_id("eduTime3").click()
        driver.find_element_by_link_text("21").click()
        driver.find_element_by_id("newEdu").click()
        time.sleep(3)
        driver.find_element_by_id("category_add").click()
        driver.find_element_by_name("ad").click()
        driver.find_element_by_css_selector("#editCategory > div.marginAuto.clearfix > a.btn.w92").click()
        driver.find_element_by_link_text(u"添加工作经历").click()
        driver.find_element_by_id("jobStartTime").click()
        driver.find_element_by_link_text("21").click()
        time.sleep(1)
        driver.find_element_by_id("jobEndTime").click()
        driver.find_element_by_link_text("26").click()
        driver.find_element_by_id("jobCompany").clear()
        driver.find_element_by_id("jobCompany").send_keys(u"第三个发货单")
        driver.find_element_by_id("jobTitle").clear()
        driver.find_element_by_id("jobTitle").send_keys(u"施工费认为他问题")
        time.sleep(1)
        driver.find_element_by_id("newJob").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"添加项目经历").click()
        driver.find_element_by_id("proName").clear()
        driver.find_element_by_id("proName").send_keys(u"为儿童要玩儿呀")
        driver.find_element_by_id("proStartTime").click()
        driver.find_element_by_link_text("11").click()
        driver.find_element_by_id("proEndTime").click()
        driver.find_element_by_link_text("28").click()
        driver.find_element_by_id("proContent").clear()
        driver.find_element_by_id("proContent").send_keys(u"二是如果二个二二二热")
        time.sleep(1)
        driver.find_element_by_id("newProSave").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"添加获奖情况").click()
        driver.find_element_by_id("awardDescription").click()
        driver.find_element_by_id("awardDescription").click()
        driver.find_element_by_id("awardDescription").clear()
        driver.find_element_by_id("awardDescription").send_keys(u"而又突然用途")
        driver.find_element_by_id("newAwardSave").click()
        driver.find_element_by_id("certBtnInfo1").click()
        #driver.find_element_by_name("file").click()
        #加入暂停10秒钟,手动输入验证码
        time.sleep(10)
        driver.find_element_by_id("certBtnInfo").click()
        driver.find_element_by_id("loginIndex").click()
    
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
        print "供应商-个人-注册搞定"
        # self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
