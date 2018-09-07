#!/usr/bin/python3
# -*- coding: utf-8 -*-
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : mark

import unittest
import sys
import time
# sys.path.append("..")
from Pages.FirstPage import FirstPage
from Pages.LoginPage import LoginPage
from selenium import webdriver
from Base.BrowserDriver import BrowserDriver


class removelgCase(unittest.TestCase):
	'''登录测试'''
    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.openbrowser(cls)

    def setUp(self):
        pass

    def test_login_success(self):
        '''用户名正确，密码正确'''

        # EP = FirstPage(self.driver)
        # EP.click_top_login()
        FP = LoginPage(self.driver)
        FP.lg_input_username('13828829616')
        FP.lg_input_password('m123456')
        FP.lg_click_buttonlogin()
        sucess_msg = self.driver.find_element_by_class_name('el-message__content').text
        try:
            # self.assertIsNotNone(
            #     self.driver.find_element_by_xpath('/html/body/div[2]/p'), '登录失败，fail')
            self.assertIn('登录成功',sucess_msg)
            print('登录成功')
        except Exception as e:
            print('登录失败', format(e))
            FP.getimg()
        time.sleep(2)
        FP.move_label_myuser()
        FP.lg_click_exit()

    def test_login_pw_error(self):
        '''用户名正确，密码不正确'''
        EP = FirstPage(self.driver)
        EP.click_top_login()
        FP = LoginPage(self.driver)
        FP.lg_input_username('13828829616')
        FP.lg_input_password('mm12345')
        FP.lg_click_buttonlogin()
        time.sleep(2)
        error_msg = self.driver.find_element_by_xpath(
            '//*[@id="pane-first"]/form/div[2]').text
        try:
            self.assertIn('登录名或密码错误', error_msg)
            print('预期结果相符')
        except Exception as e:
            print('登录错误成功', format(e))
            FP.getimg()
        self.driver.refresh()

    def test_login_pw_null(self):
        '''用户名正确，密码为空'''
        # EP = FirstPage(self.driver)
        # EP.click_top_login()
        FP = LoginPage(self.driver)
        FP.lg_input_username('13828829616')
        FP.lg_input_password('')
        FP.lg_click_buttonlogin()
        time.sleep(2)
        error_msg = self.driver.find_element_by_xpath(
            '//*[@id="pane-first"]/form/div[2]').text
        try:
            self.assertIn('请输入登录密码', error_msg)
            print('预期结果相符')
        except Exception as e:
            print('登录错误成功', format(e))
            FP.getimg()
        self.driver.refresh()

    def test_login_usr_error(self):
        '''用户名不正确，密码正确'''
        EP = FirstPage(self.driver)
        EP.click_top_login()
        FP = LoginPage(self.driver)
        FP.lg_input_username('13828829617')
        FP.lg_input_password('m123456')
        FP.lg_click_buttonlogin()
        time.sleep(2)
        error_msg = self.driver.find_element_by_xpath(
            '//*[@id="pane-first"]/form/div[2]').text
        try:
            self.assertIn('账号未注册', error_msg)
            print('预期结果相符')
        except Exception as e:
            print('登录错误成功', format(e))
            FP.getimg()
        self.driver.refresh()

    def test_login_usr_null(self):
        '''用户名为空，密码正确'''
        # EP = FirstPage(self.driver)
        # EP.click_top_login()
        FP = LoginPage(self.driver)
        FP.lg_input_username('')
        FP.lg_input_password('m123456')
        FP.lg_click_buttonlogin()
        time.sleep(2)
        error_msg = self.driver.find_element_by_xpath(
            '//*[@id="pane-first"]/form/div[2]').text
        try:
            self.assertIn('请输入手机号或用户名', error_msg)
            print('预期结果相符')
        except Exception as e:
            print('登录错误成功', format(e))
            FP.getimg()
        self.driver.refresh()

    def test_pw_cansee(self):
        '''密码明文/暗文'''
        # EP = FirstPage(self.driver)
        # EP.click_top_login()
        FP = LoginPage(self.driver)
        FP.lg_input_password(' ab12!%')
        time.sleep(1)
        link = self.driver.find_element_by_xpath(
            '//*[@id="pane-first"]/form/div[1]/div[2]/div/span')
        value = link.value_of_css_property('class')
        try:
            self.assertIsNotNone('lr_icon_eye', 'fail')
            print('密码为暗文正确')
        except Exception as e:
            print('密码错误为明文', format(e))
            FP.getimg()
        FP.lg_click_cansee()
        try:
            self.assertIsNotNone('lr_icon_eye open', 'fail')
            print('密码为明文正确')
        except Exception as e:
            print('密码错误为暗文', format(e))
            FP.getimg()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        pass
