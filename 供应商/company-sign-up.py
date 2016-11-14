# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CompanySignUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://cp.test.dongdaodao.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_company_sign_up(self):
        driver = self.driver
        driver.get(self.base_url + "/user/login")
        driver.find_element_by_link_text(u"注册").click()
        driver.find_element_by_id("companyReg").click()

        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("15333333333")
        driver.find_element_by_link_text(u"获取验证码").click()

        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("111111")
        driver.find_element_by_id("confirmPassword").clear()
        driver.find_element_by_id("confirmPassword").send_keys("111111")
        driver.find_element_by_id("agreement").click()
        #从redis数据库获取数据
        time.sleep(10)
        driver.find_element_by_id("registerBtn").click()

        driver.find_element_by_name("companyName").clear()
        driver.find_element_by_name("companyName").send_keys(u"测试公司账号")
        driver.find_element_by_name("createDate").clear()
        driver.find_element_by_name("createDate").send_keys("2000")
        Select(driver.find_element_by_id("staffSize")).select_by_visible_text(u"1000人以上")
        Select(driver.find_element_by_id("staffYearsWorking")).select_by_visible_text(u"10年以上")
        driver.find_element_by_name("registeredCapital").clear()
        driver.find_element_by_name("registeredCapital").send_keys("2000")
        driver.find_element_by_name("officialWebsite").clear()
        driver.find_element_by_name("officialWebsite").send_keys("www.baidu.com")
        driver.find_element_by_name("enterprisePhone").clear()
        driver.find_element_by_name("enterprisePhone").send_keys("010-11111111")
        time.sleep(1)
        Select(driver.find_element_by_id("provId")).select_by_visible_text(u"天津")
        time.sleep(1)
        Select(driver.find_element_by_id("areaId")).select_by_visible_text(u"南开区")
        driver.find_element_by_name("officeAddress").clear()
        driver.find_element_by_name("officeAddress").send_keys(u"三川商务园B座")
        driver.find_element_by_name("legalName").clear()
        driver.find_element_by_name("legalName").send_keys(u"测试公司供应商")
        driver.find_element_by_name("legalIdCardNo").clear()
        driver.find_element_by_name("legalIdCardNo").send_keys("371421198801210038")
        driver.find_element_by_css_selector("span.rangeSpan").click()
        driver.find_element_by_name("businessScope").click()
        driver.find_element_by_name("businessScope").clear()
        driver.find_element_by_name("businessScope").send_keys(u"测试营业范围测试营业范围测试营业范围测试营业范围测试营业范围测试营业范围测试营业范围测试营业范围测试营业范围测试营业范围测试营业范围测试营业范围测试营业范围")
        driver.find_element_by_id("companyInfo").click()
        driver.find_element_by_link_text(u"普通营业执照").click()
        driver.find_element_by_id("permit").click()

        driver.find_element_by_name("businessLicenseCode").click()
        driver.find_element_by_name("businessLicenseCode").clear()
        driver.find_element_by_name("businessLicenseCode").send_keys("371421198801210038")
        driver.find_element_by_name("organizationCode").click()
        driver.find_element_by_name("organizationCode").clear()
        driver.find_element_by_name("organizationCode").send_keys("371421198801210038")
        driver.find_element_by_name("taxID").click()
        driver.find_element_by_name("taxID").click()
        driver.find_element_by_name("taxID").clear()
        driver.find_element_by_name("taxID").send_keys("371421198801210038")
        driver.find_element_by_name("organizationCode").click()
        driver.find_element_by_name("organizationCode").clear()
        driver.find_element_by_name("organizationCode").send_keys("3714211988")
        driver.find_element_by_name("businessLicenseCode").click()
        driver.find_element_by_name("businessLicenseCode").clear()
        driver.find_element_by_name("businessLicenseCode").send_keys("371421198801211")
        driver.find_element_by_css_selector("p.uploadImg").click()
        time.sleep(20)
        # driver.find_element_by_css_selector("#rt_rt_1b11d7h4f1n111uab1moa4q068c4 > input[name=\"file\"]").click()
        # # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        # driver.find_element_by_css_selector("#sizzle-1478589924305 > p.uploadImg").click()
        # driver.find_element_by_css_selector("#rt_rt_1b11d7h4h1u4868850htke1v517 > input[name=\"file\"]").click()
        # # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        # driver.find_element_by_css_selector("#sizzle-1478589924305 > p.uploadImg").click()
        # driver.find_element_by_css_selector("#rt_rt_1b11d7h4h1u4868850htke1v517 > input[name=\"file\"]").click()
        # # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        # driver.find_element_by_css_selector("#sizzle-1478589924305 > p.uploadImg").click()
        # driver.find_element_by_css_selector("#rt_rt_1b11d7h4iij075gt1sj6hj4a > input[name=\"file\"]").click()
        # # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        # driver.find_element_by_css_selector("#sizzle-1478589924305 > p.uploadImg").click()
        # driver.find_element_by_name("file").click()
        # # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        # driver.find_element_by_css_selector("#sizzle-1478589924305 > p.uploadImg").click()
        # driver.find_element_by_name("file").click()
        # # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        driver.find_element_by_xpath("//div[@id='mainPage']/div/div").click()
        driver.find_element_by_id("saveBaseInfo").click()
        driver.find_element_by_link_text(u"添加业务优势").click()
        driver.find_element_by_xpath("(//input[@name='ad'])[2]").click()
        driver.find_element_by_link_text(u"保存").click()
        driver.find_element_by_link_text(u"添加项目经历").click()
        driver.find_element_by_id("proName").clear()
        driver.find_element_by_id("proName").send_keys(u"测试项目")
        driver.find_element_by_id("proStartTime").click()
        driver.find_element_by_link_text("10").click()
        driver.find_element_by_id("proEndTime").click()
        driver.find_element_by_link_text("24").click()
        driver.find_element_by_id("proContent").click()
        driver.find_element_by_id("proContent").click()
        driver.find_element_by_xpath("//form[@id='addPro']/div/div/div[2]/div/span").click()
        driver.find_element_by_id("proContent").click()
        driver.find_element_by_id("proContent").clear()
        driver.find_element_by_id("proContent").send_keys(u"测试项目")
        driver.find_element_by_id("proContent").click()
        driver.find_element_by_id("proContent").clear()
        driver.find_element_by_id("proContent").send_keys(u"测试项目测试项目测试项目测试项目测试项目测试项目测试项目测试项目测试项目测试项目测试项目测试项目")
        driver.find_element_by_id("newProSave").click()
        driver.find_element_by_link_text(u"添加对接人简介").click()
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(u"测试账号")
        driver.find_element_by_name("gender").click()
        driver.find_element_by_name("age").click()
        driver.find_element_by_name("age").clear()
        driver.find_element_by_name("age").send_keys("20")
        driver.find_element_by_id("provId").click()
        Select(driver.find_element_by_id("provId")).select_by_visible_text(u"重庆")
        driver.find_element_by_css_selector("option[value=\"280\"]").click()
        driver.find_element_by_id("areaId").click()
        Select(driver.find_element_by_id("areaId")).select_by_visible_text(u"江北区")
        driver.find_element_by_css_selector("option[value=\"434\"]").click()
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(u"三川商务园")
        driver.find_element_by_name("idCardNo").clear()
        driver.find_element_by_name("idCardNo").send_keys("b")
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(u"三川商务园b座")
        driver.find_element_by_name("idCardNo").clear()
        driver.find_element_by_name("idCardNo").send_keys("37")
        driver.find_element_by_name("idCardNo").click()
        driver.find_element_by_name("idCardNo").clear()
        driver.find_element_by_name("idCardNo").send_keys("371421198801210038")
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(u"设计师")
        driver.find_element_by_id("degree").click()
        Select(driver.find_element_by_id("degree")).select_by_visible_text(u"中专")
        driver.find_element_by_css_selector(u"option[value=\"中专\"]").click()
        driver.find_element_by_name("email").click()
        driver.find_element_by_id("degree").click()
        Select(driver.find_element_by_id("degree")).select_by_visible_text("EMBA")
        driver.find_element_by_css_selector("option[value=\"EMBA\"]").click()
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("1@1.com")
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("1234567890")
        driver.find_element_by_name("yearsWorking").clear()
        driver.find_element_by_name("yearsWorking").send_keys("3")
        driver.find_element_by_css_selector("#editForm > div.marginAuto.clearfix > a.btn.w92").click()
        driver.find_element_by_link_text(u"添加获奖情况").click()
        driver.find_element_by_id("awardDescription").click()
        driver.find_element_by_css_selector("div.projectAdd.projectList > div.eduAddList > p > span.rangeSpan1").click()
        driver.find_element_by_id("awardDescription").click()
        driver.find_element_by_id("awardDescription").clear()
        driver.find_element_by_id("awardDescription").send_keys(u"所获奖项所获奖项所获奖项所获奖项所获奖项所获奖项所获奖项所获奖项所获奖项所获奖项所获奖项所获奖项")
        driver.find_element_by_css_selector("#awardPart > div.resumeContent.clearfix").click()
        driver.find_element_by_id("newAwardSave").click()

        driver.find_element_by_id("certBtnInfo1").click()
        time.sleep(5)
        # driver.find_element_by_name("file").click()
        # # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
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
        print "公司注册完成"
        # self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
