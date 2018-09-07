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
from selenium.webdriver.support import expected_conditions as EC


class moveuserCase(unittest.TestCase):
	'''我的账号下拉标签跳转'''
	@classmethod
	def setUpClass(cls):
		driver = BrowserDriver(cls)
		cls.driver = driver.openbrowser(cls)

	def setUp(self):
		pass

	def test_moveuser(self):
		'''跳转至账号概览'''
		FP = FirstPage(self.driver)
		# FP.click_top_login()
		title = EC.title_is('账户概览')
		if title(self.driver) == True:
			FP.move_label_myuser()  # 悬浮我的账号
			FP.click_labelmu_thing()  # 点击账号概览
			try:
				FP.istitle('账户概览')
				print('实际结果与预期相符')
			except Exception as e:
				print('跳转至账号概览失败！！', format(e))
				FP.getimg()
			self.driver.back()
		else:
			EP = LoginPage(self.driver)
			EP.lg_input_username('13828829616')
			EP.lg_input_password('m123456')
			EP.lg_click_buttonlogin()
			FP.move_label_myuser()  # 悬浮我的账号
			FP.click_labelmu_thing()  # 点击账号概览
			try:
				FP.istitle('账户概览')
				print('实际结果与预期相符')
			except Exception as e:
				print('跳转至账号概览失败！！', format(e))
				FP.getimg()
			self.driver.back()	

	def test_movepay(self):
		'''跳转至我的出借'''
		FP = FirstPage(self.driver)
		# FP.click_top_login()
		title = EC.title_is('账户概览')
		if title(self.driver) == True:
			FP.move_label_myuser()  # 悬浮我的账号
			FP.click_labelmu_touzi()  # 点击我的出借
			try:
				FP.istitle('我的出借')
				print('实际结果与预期相符')
			except Exception as e:
				print('跳转至我的出借失败！！', format(e))
				FP.getimg()
			self.driver.back()
		else:
			EP = LoginPage(self.driver)
			EP.lg_input_username('13828829616')
			EP.lg_input_password('m123456')
			EP.lg_click_buttonlogin()
			FP.move_label_myuser()  # 悬浮我的账号
			FP.click_labelmu_touzi()  # 点击我的出借
			try:
				FP.istitle('我的出借')
				print('实际结果与预期相符')
			except Exception as e:
				print('跳转至我的出借失败！！', format(e))
				FP.getimg()
			self.driver.back()

	# def test_movebrower(self):
	# 	'''跳转至我的借款'''
	#
	# 	FP = FirstPage(self.driver)
	# 	FP.click_top_login()
	# 	title = EC.title_is('账户概览')
	# 	if title(self.driver) == True:
	# 		FP.move_label_myuser()  # 悬浮我的账号
	# 		FP.click_labelmu_jiekuan()  # 点击我的借款
	# 		try:
	# 			FP.istitle('我的借款')
	# 			print('实际结果与预期相符')
	# 		except Exception as e:
	# 			print('跳转至我的借款失败！！',format(e))
	# 			FP.getimg()
	# 		self.driver.back()
	# 	else:
	# 		EP = LoginPage(self.driver)
	# 		EP.lg_input_username('13828829616')
	# 		EP.lg_input_password('m123456')
	# 		EP.lg_click_buttonlogin()
	# 		FP.move_label_myuser()  # 悬浮我的账号
	# 		FP.click_labelmu_jiekuan()  # 点击我的借款
	# 		try:
	# 			FP.istitle('我的借款')
	# 			print('实际结果与预期相符')
	# 		except Exception as e:
	# 			print('跳转至我的借款失败！！',format(e))
	# 			FP.getimg()
	# 		self.driver.back()
	#
	# def test_movepaylog(self):
	# 	'''跳转至交易记录'''
	# 	FP = FirstPage(self.driver)
	# 	# FP.click_top_login()
	# 	title = EC.title_is('账户概览')
	# 	if title(self.driver) == True:
	# 		FP.move_label_myuser()#悬浮我的账号
	# 		FP.click_labelmu_paylogs()#点击交易记录
	# 		try:
	# 			FP.istitle('交易记录')
	# 			print('实际结果与预期相符')
	# 		except Exception as e:
	# 			print('跳转至交易记录失败！！',format(e))
	# 			FP.getimg()
	# 		self.driver.back()
	# 	else:
	# 		EP = LoginPage(self.driver)
	# 		EP.lg_input_username('13828829616')
	# 		EP.lg_input_password('m123456')
	# 		EP.lg_click_buttonlogin()
	# 		FP.move_label_myuser()#悬浮我的账号
	# 		FP.click_labelmu_paylogs()#点击交易记录
	# 		try:
	# 			FP.istitle('交易记录')
	# 			print('实际结果与预期相符')
	# 		except Exception as e:
	# 			print('跳转至交易记录失败！！',format(e))
	# 			FP.getimg()
	# 		self.driver.back()
	#
	# def test_movesetting(self):
	# 	'''跳转至账号设置'''
	# 	FP = FirstPage(self.driver)
	# 	# FP.click_top_login()
	# 	title = EC.title_is('账户概览')
	# 	if title(self.driver) == True:
	# 		FP.move_label_myuser()#悬浮我的账号
	# 		FP.click_labelmu_shezhi()#点击账户安全
	# 		try:
	# 			FP.istitle('账户安全')
	# 			print('实际结果与预期相符')
	# 		except Exception as e:
	# 			print('跳转至账户安全失败！！',format(e))
	# 			FP.getimg()
	# 		self.driver.back()
	# 	else:
	# 		EP = LoginPage(self.driver)
	# 		EP.lg_input_username('13828829616')
	# 		EP.lg_input_password('m123456')
	# 		EP.lg_click_buttonlogin()
	# 		FP.move_label_myuser()#悬浮我的账号
	# 		FP.click_labelmu_shezhi()#点击账户安全
	# 		try:
	# 			FP.istitle('账户安全')
	# 			print('实际结果与预期相符')
	# 		except Exception as e:
	# 			print('跳转至账户安全失败！！',format(e))
	# 			FP.getimg()
	# 		self.driver.back()
	#
	# def test_movekaquan(self):
	# 	'''跳转至我的卡券'''
	# 	FP = FirstPage(self.driver)
	# 	FP.click_top_login()
	# 	title = EC.title_is('账户概览')
	# 	if title(self.driver) == True:
	# 		FP.move_label_myuser()#悬浮我的账号
	# 		FP.click_labelmu_kaquan()#点击我的卡券
	# 		try:
	# 			FP.istitle('我的卡券')
	# 			print('实际结果与预期相符')
	# 		except Exception as e:
	# 			print('跳转至我的卡券失败！！',format(e))
	# 			FP.getimg()
	# 		self.driver.back()
	# 	else:
	# 		EP = LoginPage(self.driver)
	# 		EP.lg_input_username('13828829616')
	# 		EP.lg_input_password('m123456')
	# 		EP.lg_click_buttonlogin()
	# 		FP.move_label_myuser()#悬浮我的账号
	# 		FP.click_labelmu_kaquan()#点击我的卡券
	# 		try:
	# 			FP.istitle('我的卡券')
	# 			print('实际结果与预期相符')
	# 		except Exception as e:
	# 			print('跳转至我的卡券失败！！',format(e))
	# 			FP.getimg()
	# 		self.driver.back()
	#
	#
	# def test_moveyaoqing(self):
	# 	'''跳转至我的邀请'''
	# 	FP = FirstPage(self.driver)
	# 	# EP.click_top_login()
	# 	# title = EC.title_is('账户概览')
	# 	# if title(self.driver) == True:
	# 	FP.move_label_myuser()#悬浮我的账号
	# 	FP.click_labelmu_yaoqing()#点击我的邀请
	# 	try:
	# 		FP.istitle('我的邀请')
	# 		print('实际结果与预期相符')
	# 	except Exception as e:
	# 		print('跳转至我的邀请失败！！',format(e))
	# 		FP.getimg()
	# 	self.driver.back()
		# else:
		# 	EP = LoginPage(self.driver)
		# 	EP.lg_input_username('13828829616')
		# 	EP.lg_input_password('m123456')
		# 	EP.lg_click_buttonlogin()
		# 	FP.move_label_myuser()#悬浮我的账号
		# 	FP.click_labelmu_yaoqing()#点击我的邀请
		# 	try:
		# 		FP.istitle('我的邀请')
		# 		print('实际结果与预期相符')
		# 	except Exception as e:
		# 		print('跳转至我的邀请失败！！',format(e))
		# 		FP.getimg()
		# 	self.driver.back()



	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def tearDown(self):
		pass
