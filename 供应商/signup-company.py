# -*- coding: utf-8 -*-
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class SignupCompany(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://cp.idaodao.net"
        # self.base_url = "http://cp.verify.idaodao.net"
        # self.base_url = "http://cp.test.dongdaodao.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_signup_company(self):
        driver = self.driver
        driver.get(self.base_url + "/user/register/view")
        driver.find_element_by_id("companyReg").click()
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("185611"+bytes(random.randint(10000, 99999)))
        driver.find_element_by_id("phoneCode").clear()
        driver.find_element_by_id("phoneCode").send_keys("1234")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("111111")
        driver.find_element_by_id("confirmPassword").clear()
        driver.find_element_by_id("confirmPassword").send_keys("111111")

        driver.find_element_by_id("agreement").click()
        #暂停，输入验证码，点注册按钮
        time.sleep(5)

        driver.find_element_by_name("companyName").clear()
        driver.find_element_by_name("companyName").send_keys(u"你说的啊")
        driver.find_element_by_name("createDate").clear()
        driver.find_element_by_name("createDate").send_keys("2005")
        Select(driver.find_element_by_id("staffSize")).select_by_visible_text(u"300-999人")
        Select(driver.find_element_by_id("staffYearsWorking")).select_by_visible_text(u"1-5年")
        driver.find_element_by_name("registeredCapital").clear()
        driver.find_element_by_name("registeredCapital").send_keys("6666")
        driver.find_element_by_name("officialWebsite").clear()
        driver.find_element_by_name("officialWebsite").send_keys("www.baidu.com")
        driver.find_element_by_name("enterprisePhone").clear()
        driver.find_element_by_name("enterprisePhone").send_keys("010-12345678")
        Select(driver.find_element_by_id("provId")).select_by_visible_text(u"广西")
        Select(driver.find_element_by_id("areaId")).select_by_visible_text(u"贵港")
        driver.find_element_by_name("officeAddress").clear()
        driver.find_element_by_name("officeAddress").send_keys(u"水电费都发生过多个鬼地方和")
        driver.find_element_by_name("legalName").clear()
        driver.find_element_by_name("legalName").send_keys(u"水电费都发")
        driver.find_element_by_name("legalIdCardNo").clear()
        driver.find_element_by_name("legalIdCardNo").send_keys("371421198801210038")
        driver.find_element_by_name("officeAddress").click()
        driver.find_element_by_name("businessScope").clear()
        driver.find_element_by_name("businessScope").send_keys(u"水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和水电费都发生过多个鬼地方和")
        driver.find_element_by_id("companyInfo").click()
        driver.find_element_by_name("businessLicenseCode").click()
        driver.find_element_by_name("businessLicenseCode").clear()
        driver.find_element_by_name("businessLicenseCode").send_keys(u"阿斯顿阿斯顿")
        driver.find_element_by_css_selector("#THR > div.editList.clearfix").click()
        driver.find_element_by_name("businessLicenseCode").click()
        driver.find_element_by_name("legalIdCardNo").click()
        driver.find_element_by_name("businessLicenseCode").click()
        driver.find_element_by_name("businessLicenseCode").clear()
        driver.find_element_by_name("businessLicenseCode").send_keys("371421198801210038")
        driver.find_element_by_css_selector("#THR > div.editList.clearfix").click()
        driver.find_element_by_name("organizationCode").click()
        driver.find_element_by_name("organizationCode").clear()
        driver.find_element_by_name("organizationCode").send_keys("371421198801210038")
        driver.find_element_by_name("taxID").click()
        driver.find_element_by_name("taxID").clear()
        driver.find_element_by_name("taxID").send_keys("371421198801210038")
        driver.find_element_by_name("organizationCode").click()
        driver.find_element_by_name("organizationCode").clear()
        driver.find_element_by_name("organizationCode").send_keys("3714211988")
        driver.find_element_by_name("businessLicenseCode").click()
        driver.find_element_by_name("businessLicenseCode").clear()
        driver.find_element_by_name("businessLicenseCode").send_keys("371421198801210")

        #手动上传图片，暂停30秒
        time.sleep(10)
        #driver.find_element_by_css_selector("p.uploadImg").click()

        # driver.find_element_by_css_selector("#rt_rt_1aurcliv2ppr18oll4irr6qof4 > input[name=\"file\"]").click()
        # # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        # driver.find_element_by_css_selector("#sizzle-1476240526240 > p.uploadImg").click()
        # driver.find_element_by_css_selector("#rt_rt_1aurcliv41oah1ajlbuj1s928t7 > input[name=\"file\"]").click()
        # # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        # driver.find_element_by_css_selector("#sizzle-1476240526240 > p.uploadImg").click()
        # driver.find_element_by_css_selector("#rt_rt_1aurcliv61k961g0ma2l5g79t0a > input[name=\"file\"]").click()
        # # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        # driver.find_element_by_css_selector("#sizzle-1476240526240 > p.uploadImg").click()
        # driver.find_element_by_name("file").click()
        # # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        # driver.find_element_by_css_selector("#sizzle-1476240526240 > p.uploadImg").click()
        # driver.find_element_by_name("file").click()
        # # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        # driver.find_element_by_id("saveBaseInfo").click()
        driver.find_element_by_link_text(u"添加业务优势").click()
        driver.find_element_by_xpath("(//input[@name='ad'])[2]").click()
        driver.find_element_by_link_text(u"保存").click()
        driver.find_element_by_link_text(u"添加项目经历").click()
        driver.find_element_by_id("proName").clear()
        driver.find_element_by_id("proName").send_keys(u"是短发飞是的f")
        driver.find_element_by_id("proStartTime").click()
        driver.find_element_by_link_text("18").click()
        driver.find_element_by_id("proEndTime").click()
        driver.find_element_by_link_text("25").click()
        driver.find_element_by_id("proContent").clear()
        driver.find_element_by_id("proContent").send_keys(u"啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高啥地方是梵蒂冈发送到高")
        driver.find_element_by_id("newProSave").click()
        driver.find_element_by_id("opr_add").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(u"阿斯蒂芬")
        driver.find_element_by_name("gender").click()
        driver.find_element_by_name("age").clear()
        driver.find_element_by_name("age").send_keys("34")
        Select(driver.find_element_by_id("provId")).select_by_visible_text(u"广西")
        Select(driver.find_element_by_id("areaId")).select_by_visible_text(u"玉林")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(u"啥地方是梵蒂冈发送到高")
        driver.find_element_by_name("idCardNo").clear()
        driver.find_element_by_name("idCardNo").send_keys("371421198801210038")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(u"该如何挂号费")
        Select(driver.find_element_by_id("degree")).select_by_visible_text(u"中专")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("234234@srefsdf.com")
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("18751232231")
        driver.find_element_by_name("yearsWorking").clear()
        driver.find_element_by_name("yearsWorking").send_keys("20")
        driver.find_element_by_css_selector("#editForm > div.marginAuto.clearfix > a.btn.w92").click()
        driver.find_element_by_link_text(u"添加获奖情况").click()
        driver.find_element_by_id("awardDescription").click()
        driver.find_element_by_id("awardDescription").clear()
        driver.find_element_by_id("awardDescription").send_keys(u"大师傅打发斯蒂芬是打发斯蒂芬")
        driver.find_element_by_id("newAwardSave").click()
        # time.sleep(30)

        driver.find_element_by_id("certBtnInfo1").click()
        #暂停10秒，上传资料
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
        print "供应商-企业-注册搞定"
        # self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
