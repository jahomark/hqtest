#!/usr/bin/python3
# -*- coding: utf-8 -*-
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : mark

# import sys
from selenium.webdriver.common.by import By
# sys.path.append("..")
from Base.Selenium2 import BasePage

class LoginPage(BasePage):
	'''页面元素定位'''
	lg_username = (By.XPATH,'//*[@id="pane-first"]/form/div[1]/div[1]/div/div/input')
	lg_password = (By.XPATH,'//*[@id="pane-first"]/form/div[1]/div[2]/div/div/input')
	lg_cansee = (By.XPATH,'//*[@id="pane-first"]/form/div[1]/div[2]/div/span')
	lg_buttonlogin = (By.XPATH,'//*[@id="pane-first"]/form/div[3]/div')
	lg_forgetpw = (By.XPATH,'/html/body/div/div[3]/div/form/div/p/a[1]')
	lg_zhuce = (By.XPATH,'/html/body/div/div[3]/div/form/div/p/a[2]')
	lg_exit = (By.CLASS_NAME,'icon7')
	label_myuser = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div[2]/a') #标签我的账号	

	def lg_input_username(self,text):
		self.send_key(self.lg_username, text)

	def lg_input_password(self,text):
		self.send_key(self.lg_password, text)

	def lg_click_cansee(self):
		self.click(self.lg_cansee)

	def lg_click_buttonlogin(self):
		self.click(self.lg_buttonlogin)

	def lg_click_forgetpw(self):
		self.click(self.lg_forgetpw)

	def lg_click_zhuce(self):
		self.click(self.lg_zhuce)

	def lg_click_exit(self):
		self.click(self.lg_exit)
		
	def getimg(self):
		self.get_screent_img()

	def move_label_myuser(self):	
		self.move_to_element(self.label_myuser)		#悬浮