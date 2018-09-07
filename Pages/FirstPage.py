#!/usr/bin/python3
# -*- coding: utf-8 -*-
# import sys
from selenium.webdriver.common.by import By
# sys.path.append("..")
from Base.Selenium2 import BasePage

class FirstPage(BasePage):

	
	top_login = (By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/div[2]/a[1]') #顶部登录
	top_zhuce = (By.XPATH,'/html/body/div/div[2]/div/div[2]/a[2]') #顶部注册
	top_help = (By.XPATH,'/html/body/div/div[2]/div/div[2]/a[3]') #顶部帮助中心
	top_about = (By.XPATH,'/html/body/div/div[2]/div/div[2]/a[4]') #顶部平台公告
	top_appdownload = (By.XPATH,'/html/body/div/div[2]/div/div[2]/span') #顶部APP下载
	label_logo = (By.XPATH,'/html/body/div/div[3]/div/div[1]/a/img') #导航栏logo
	label_frist = (By.XPATH,'/html/body/div/div[3]/div/div[2]/a[1]/span') #标签首页
	label_dq = (By.XPATH,'/html/body/div/div[3]/div/div[2]/a[2]/span')#标签定期
	label_abus = (By.XPATH,'/html/body/div/div[3]/div/div[2]/a[3]/span') #标签关于我们
	label_safe = (By.XPATH,'/html/body/div/div[3]/div/div[2]/a[4]/span') #标签安全保障
	label_myuser = (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div[2]/a') #标签我的账号
	labelmu_thing = (By.XPATH,'/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/ul/a[1]/li') #下拉选项账号概况
	labelmu_touzi = (By.XPATH,'/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/ul/a[2]/li') #下拉选项我的出借
	labelmu_jiekuan = (By.XPATH,'/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/ul/a[3]/li')#下拉选项我的借款
	labelmu_paylogs = (By.XPATH,'/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/ul/a[4]/li') #下拉选项交易记录
	labelmu_shezhi = (By.XPATH,'/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/ul/a[5]/li') #下拉选项账号安全
	labelmu_kaquan = (By.XPATH,'/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/ul/a[6]/li') #下拉选项我的卡券
	labelmu_yaoqing = (By.XPATH,'/html/body/div/div/div[1]/div[2]/div/div[2]/div[2]/ul/a[7]/li') #下拉选项我的邀请
	button_zhuce = (By.XPATH,'/html/body/div/div[4]/div[1]/div[2]/div[1]/a')#正文按钮注册
	button_login = (By.XPATH,'/html/body/div/div[4]/div[1]/div[2]/div[1]/p/a')#正文按钮登录
	button2_login = (By.XPATH,'/html/body/div/div[4]/div[1]/div[2]/div[2]/form/div/div[4]/input')#登录入口
	right_talk = (By.XPATH,'/html/body/div/div[1]/div[1]')#右侧联系客服
	right_backtop = (By.XPATH,'/html/body/div/div[1]/div[2]/span')#右侧返回顶部
	qkpay_fr = (By.XPATH,'/html/body/div/div[4]/div[3]/div/div/ul/li[1]/div[2]/a')#第一个标的投资
	qkpay_se = (By.XPATH,'/html/body/div/div[4]/div[3]/div/div/ul/li[2]/div[2]/a')#第二个标的投资
	qkpay_th = (By.XPATH,'/html/body/div/div[4]/div[3]/div/div/ul/li[3]/div[2]/a')#第三个标的投资
	qkpay_all = (By.XPATH,'/html/body/div/div[4]/div[3]/div/div/ul/li[4]/div/a')#更多的标的投资
	new_all = (By.XPATH,'/html/body/div/div[4]/div[4]/div/a')#查看更多新闻
	help_jfpt = (By.XPATH,'/html/body/div/div[5]/div/div[1]/div/dl[1]/dd[1]/a')#帮助中心-金服平台
	help_zhgl = (By.XPATH,'/html/body/div/div[5]/div/div[1]/div/dl[1]/dd[2]/a')#帮助中心-账号管理
	help_zjgl = (By.XPATH,'/html/body/div/div[5]/div/div[1]/div/dl[1]/dd[3]/a')#帮助中心-资金管理
	help_tzcp = (By.XPATH,'/html/body/div/div[5]/div/div[1]/div/dl[1]/dd[4]/a')#帮助中心-投资产品
	help_wdkq = (By.XPATH,'/html/body/div/div[5]/div/div[1]/div/dl[1]/dd[5]/a')#帮助中心-我的卡券
	help_yqhy = (By.XPATH,'/html/body/div/div[5]/div/div[1]/div/dl[1]/dd[6]/a')#帮助中心-邀请好友
	about_gyzm = (By.XPATH,'/html/body/div/div[5]/div/div[1]/div/dl[2]/dd[1]/a')#关于我们-关于众美
	about_xwdt = (By.XPATH,'/html/body/div/div[5]/div/div[1]/div/dl[2]/dd[2]/a')#关于我们-新闻动态
	about_wzgg = (By.XPATH,'/html/body/div/div[5]/div/div[1]/div/dl[2]/dd[3]/a')#关于我们-网站公告
	about_aqbz = (By.XPATH,'/html/body/div/div[5]/div/div[1]/div/dl[2]/dd[4]/a')#关于我们-安全保障
	about_lxwm = (By.XPATH,'/html/body/div/div[5]/div/div[1]/div/dl[2]/dd[5]/a')#关于我们-联系我们

	def get(self):
		self.get_page_title()
	def scroll_middle(self):
		self.js_scroll_middle()
	def get_weburl(self):
		self.get_url()
		
	
	def scroll_end(self):
		self.js_scroll_end()

	def getimg(self):
		self.get_screent_img()

	def switch(self):
		self.switch_windows()

	def istitle(self,title):
		self.is_title(title, timeout=10)

	def istitle_cantains(self,title):
		self.is_title_contains(title, timeout=10)

	def click_top_login(self):
		self.click(self.top_login)
	
	def click_top_zhuce(self):
		self.click(self.top_zhuce)
	
	def click_top_help(self):
		self.click(self.top_help)
	
	def click_top_about(self):
		self.click(self.top_about)

	def move_top_appdownload(self):
		self.move_to_element(self.top_appdownload)   #悬浮元素
	
	def click_label_logo(self):
		self.click(self.label_logo)

	def click_label_frist(self):
		self.click(self.label_frist)

	def click_label_dq(self):
		self.click(self.label_dq)	

	def click_label_abus(self):
		self.click(self.label_abus)

	def click_label_safe(self):
		self.click(self.label_safe)

	def click_label_myuser(self):
		self.click(self.label_myuser)

	def move_label_myuser(self):	
		self.move_to_element(self.label_myuser)		#悬浮

	def click_labelmu_thing(self):
		self.click(self.labelmu_thing)

	def click_labelmu_touzi(self):
		self.click(self.labelmu_touzi)

	def click_labelmu_jiekuan(self):
		self.click(self.labelmu_jiekuan)

	def click_labelmu_kaquan(self):
		self.click(self.labelmu_kaquan)

	def click_labelmu_yaoqing(self):
		self.click(self.labelmu_yaoqing)

	def click_labelmu_paylogs(self):
		self.click(self.labelmu_paylogs)

	def click_labelmu_shezhi(self):
		self.click(self.labelmu_shezhi)	

	def click_button_zhuce(self):
		self.click(self.button_zhuce)

	def click_button_login(self):
		self.click(self.button_login)

	def click_button2_login(self):
		self.click(self.button2_login)	

	def move_right_talk(self):
		self.move_to_element(self.right_talk)#悬浮

	def click_right_backtop(self):
		self.click(self.right_backtop)

	def click_qkpay_fr(self):
		self.click(self.qkpay_fr)	

	def click_qkpay_se(self):
		self.click(self.qkpay_se)	

	def click_qkpay_th(self):
		self.click(self.qkpay_th)	

	def click_qkpay_all(self):
		self.click(self.qkpay_all)

	def click_new_all(self):
		self.click(self.new_all)	

	def click_help_jfpt(self):
		self.click(self.help_jfpt)	

	def click_help_zhgl(self):
		self.click(self.help_zhgl)	

	def click_help_zjgl(self):
		self.click(self.help_zjgl)	

	def click_help_tzcp(self):
		self.click(self.help_tzcp)	

	def click_help_wdkq(self):
		self.click(self.help_wdkq)	

	def click_help_yqhy(self):
		self.click(self.help_yqhy)	

	def click_about_gyzm(self):
		self.click(self.about_gyzm)	

	def click_about_xwdt(self):
		self.click(self.about_xwdt)	

	def click_about_wzgg(self):
		self.click(self.about_wzgg)	

	def click_about_aqbz(self):
		self.click(self.about_aqbz)	

	def click_about_lxwm(self):
		self.click(self.about_lxwm)	
