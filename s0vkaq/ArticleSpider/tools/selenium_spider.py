# -*- coding: utf-8 -*-

from selenium import webdriver
from scrapy.selector import Selector


#知乎的模拟登录
# browser = webdriver.Chrome(executable_path="E:/chromedriver.exe")  #路径是chromedriver.exe的存放的位置
# browser.get("https://www.zhihu.com/#signin")
# browser.find_element_by_css_selector(".view-signin input[name='account']").send_keys("********") #帐号
# browser.find_element_by_css_selector(".view-signin input[name='password']").send_keys("********") #密码
# browser.find_element_by_id("captcha").send_keys(input('请输入验证码：'))
# browser.find_element_by_css_selector(".view-signin button.sign-button").click() #登录
# browser.quit()
#
#
# #可以用selenium得到js加载后的html，比如这样的话可以抓取到本来抓取的不到的一些字段（淘宝的交易量等等）
# browser = webdriver.Chrome(executable_path="E:/chromedriver.exe")
# browser.get("https://detail.tmall.com/item.htm?spm=a230r.1.14.3.yYBVG6&id=538286972599&cm_id=140105335569ed55e27b&abbucket=15&sku_properties=10004:709990523;5919063:6536025")
# print(browser.page_source) #page_source就是js加载完的源代码
# #browser.quit()
# '''
# 如果是用selenium本身的选择器（python写的，比较慢），会很慢
# 所以现在转换成scrapy中的selector（他是用c语言写的，很快）
# 模版，也可以嵌入scrapy中
# '''
# t_selector=Selector(text=browser.page_source)
# print(t_selector.xpath('//*[@id="J_StrPriceModBox"]/dd/span/text()').extract())


# #selenium 完成微博模拟登录
# browser = webdriver.Chrome(executable_path="E:/chromedriver.exe")
# browser.get("http://weibo.com/")
# import time
# time.sleep(5)
# browser.find_element_by_css_selector("#loginname").send_keys("******")
# browser.find_element_by_css_selector(".info_list.password input[node-type='password']").send_keys("******")
# browser.find_element_by_css_selector(".info_list.login_btn a[node-type='submitBtn']").click()
# #下拉
# for i in range(3):
#     '''三次下拉操作，这是javascript的知识'''
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
#     time.sleep(3)


#设置chromedriver不加载图片
#是固定的模版
# chrome_opt = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chrome_opt.add_experimental_option("prefs", prefs)
# browser = webdriver.Chrome(executable_path="E:/chromedriver.exe",chrome_options=chrome_opt)
# browser.get("http://weibo.com/")


#phantomjs, 无界面的浏览器， 多进程情况下phantomjs性能会下降很严重
browser = webdriver.PhantomJS(executable_path="F:/迅雷下载/phantomjs-2.1.1-windows/bin/phantomjs.exe")
browser.get("https://detail.tmall.com/item.htm?spm=a230r.1.14.3.yYBVG6&id=538286972599&cm_id=140105335569ed55e27b&abbucket=15&sku_properties=10004:709990523;5919063:6536025")
print (browser.page_source)
browser.quit()