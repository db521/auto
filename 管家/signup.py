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
        # self.base_url = "http://k.idaodao.net"
        # self.base_url = "http://k.verify.idaodao.net"
        self.base_url = "http://k.test.dongdaodao.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_signup(self):
        driver = self.driver
        driver.get(self.base_url + "/user/auth/login")
        driver.find_element_by_link_text(u"注册").click()
        driver.find_element_by_id("phone").clear()
        #18911888540为道道生产环境注册账号
        # driver.find_element_by_id("phone").send_keys("18911888540")


        driver.find_element_by_id("phone").send_keys("185617"+bytes(random.randint(10000, 99999)))
        driver.find_element_by_id("smCaptcha").clear()
        driver.find_element_by_id("smCaptcha").send_keys("1234")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("111111")
        driver.find_element_by_id("confirmPassword").clear()
        driver.find_element_by_id("confirmPassword").send_keys("111111")

        driver.find_element_by_id("agreeCheckbox").click()
        #手动输入验证码
        time.sleep(5)
        #第一页
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(u"我是管家")
        driver.find_element_by_name("gender").click()
        driver.find_element_by_id("yearsWorking").clear()
        driver.find_element_by_id("yearsWorking").send_keys("20")
        Select(driver.find_element_by_id("provId")).select_by_visible_text(u"天津")
        Select(driver.find_element_by_id("areaId")).select_by_visible_text(u"河东区")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(u"三川商务园B座")
        driver.find_element_by_name("idCardNo").clear()
        driver.find_element_by_name("idCardNo").send_keys("371421198801210038")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("121212@qq.com")
        # 手动选择图片上传
        time.sleep(5)

        driver.find_element_by_id("saveBaseInfo").click()
        #第二页
        driver.find_element_by_link_text(u"添加教育经历").click()
        driver.find_element_by_id("school").clear()
        driver.find_element_by_id("school").send_keys(u"北京大学")
        driver.find_element_by_id("major").clear()
        driver.find_element_by_id("major").send_keys(u"计算机科学与技术")
        Select(driver.find_element_by_id("degree")).select_by_visible_text(u"博士")
        driver.find_element_by_id("eduTime2").click()
        driver.find_element_by_link_text("19").click()
        driver.find_element_by_id("eduTime3").click()
        driver.find_element_by_link_text("19").click()
        driver.find_element_by_id("newEdu").click()
        driver.find_element_by_link_text(u"添加业务优势").click()
        driver.find_element_by_name("ad").click()
        driver.find_element_by_css_selector("#editCategory > div.marginAuto.clearfix > a.btn.w92").click()
        driver.find_element_by_link_text(u"添加工作经历").click()
        driver.find_element_by_id("jobStartTime").click()
        driver.find_element_by_link_text("13").click()
        driver.find_element_by_id("jobEndTime").click()
        driver.find_element_by_link_text("14").click()
        driver.find_element_by_id("jobCompany").clear()
        driver.find_element_by_id("jobCompany").send_keys(u"东道设计")
        driver.find_element_by_id("jobTitle").clear()
        driver.find_element_by_id("jobTitle").send_keys(u"设计总监")
        driver.find_element_by_id("newJob").click()
        driver.find_element_by_link_text(u"添加项目经历").click()
        driver.find_element_by_id("proName").clear()
        driver.find_element_by_id("proName").send_keys(u"广发证券LOGO设计")
        driver.find_element_by_id("proStartTime").click()
        driver.find_element_by_link_text("19").click()
        driver.find_element_by_id("proEndTime").click()
        driver.find_element_by_link_text("20").click()
        driver.find_element_by_id("proContent").click()
        driver.find_element_by_id("proContent").click()
        driver.find_element_by_id("proContent").clear()
        driver.find_element_by_id("proContent").send_keys(u"设计方案:东道在原有logo的基础上进行调整，使新logo既继承了原logo的风格，又注入了活力、增添了时代感，彰显广发证券的国际化和专业化。标识外形和色彩调整后，'广'字的首字母'G'的识别性也大大加强。调整使得中心部位有了更多空间，更加通透灵动。标识中'F'图形通过调整增加了一个转折的结构，使其更加流畅有力，体量感增强，稳重大气。标识外部图形和中部的'F' 都采用了渐变效果，形成明暗对比，体现出标识整体的和谐之美。")


        # driver.find_element_by_id("proContent").send_keys(u"样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样他他也同样")
        # driver.find_element_by_id("newProSave").click()
        # driver.find_element_by_id("certBtnInfo").click()
        # driver.find_element_by_id("loginIndex").click()
        #
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
        print "管家注册成功"
        # self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
