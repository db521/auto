# -*- coding: utf-8 -*-
import random

from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

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
        #18515430674为黄鑫，线上供应商注册号
        # driver.find_element_by_id("phone").send_keys("18515430674")
        #18211100049为黄鑫，线上供应商注册号
        # driver.find_element_by_id("phone").send_keys("18211100049")
        # 18811510575为赵尚，线上供应商注册号
        driver.find_element_by_id("phone").send_keys("18811510575")

        # driver.find_element_by_id("phone").send_keys("185616"+bytes(random.randint(10000, 99999)))
        driver.find_element_by_id("phoneCode").clear()
        driver.find_element_by_id("phoneCode").send_keys("1234")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("111111")
        driver.find_element_by_id("confirmPassword").clear()
        driver.find_element_by_id("confirmPassword").send_keys("111111")
        driver.find_element_by_id("agreement").click()

        #加入暂停10秒钟,手动输入验证码
        time.sleep(10)

        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(u"供应商三")
        driver.find_element_by_id("yearsWorking").clear()
        driver.find_element_by_id("yearsWorking").send_keys("2")
        driver.find_element_by_name("gender").click()
        driver.find_element_by_id("yearsWorking").clear()
        driver.find_element_by_id("yearsWorking").send_keys("23")
        Select(driver.find_element_by_id("provId")).select_by_visible_text(u"北京")
        Select(driver.find_element_by_id("areaId")).select_by_visible_text(u"朝阳区")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(u"三川商务园B座")
        driver.find_element_by_name("idCardNo").clear()
        driver.find_element_by_name("idCardNo").send_keys("371421198801210038")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("1154833834@qq.com")

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
        driver.find_element_by_id("school").send_keys(u"清华大学")
        Select(driver.find_element_by_id("degree")).select_by_visible_text(u"博士")
        driver.find_element_by_id("major").clear()
        driver.find_element_by_id("major").send_keys(u"平面设计")
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
        driver.find_element_by_id("jobCompany").send_keys(u"东道设计")
        driver.find_element_by_id("jobTitle").clear()
        driver.find_element_by_id("jobTitle").send_keys(u"高级设计师")
        time.sleep(1)
        driver.find_element_by_id("newJob").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"添加项目经历").click()
        driver.find_element_by_id("proName").clear()
        driver.find_element_by_id("proName").send_keys(u"金杯LOGO")
        driver.find_element_by_id("proStartTime").click()
        driver.find_element_by_link_text("11").click()
        driver.find_element_by_id("proEndTime").click()
        driver.find_element_by_link_text("28").click()
        driver.find_element_by_id("proContent").clear()
        driver.find_element_by_id("proContent").send_keys(u"基于东道与金杯管理层的深度访谈，项目团队对于汽车行业的深入了解，通过实地厂区、销售店形象调研，遵循东道'发现、创造规范管理'的系统方法:东道针对金杯原标志形象，对标志提出了微调提升的建议，延续金杯多年以来的品牌积淀 对金杯品牌标准字体，进行了重新设计，充满了力量感与现代品质，符合金杯汽车致力于打造具有影响力的国际化品牌气质 .")
        time.sleep(1)
        driver.find_element_by_id("newProSave").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"添加获奖情况").click()
        driver.find_element_by_id("awardDescription").click()
        driver.find_element_by_id("awardDescription").click()
        driver.find_element_by_id("awardDescription").clear()
        driver.find_element_by_id("awardDescription").send_keys(u" 其它荣获奖项的作品包括获得'设计未来世界奖'的Tesla Model S，世界上第一款全尺寸高性能电动轿车;获得'最佳可持续奖'的宝马i3，宝马第一辆只靠电力驱动的汽车，100%使用可再生能源;此外，还有把用户放在设计的前端和核心的最佳数码设计奖得主Uber。")
        driver.find_element_by_id("newAwardSave").click()
        driver.find_element_by_id("certBtnInfo1").click()
        #driver.find_element_by_name("file").click()
        #加入暂停10秒钟,手动上传文件
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
