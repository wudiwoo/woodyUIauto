from selenium import webdriver
from bs4 import BeautifulSoup
from web_drivers import  get_web_driver

# 使用 Chrome 浏览器驱动程序
browser='chrome'
driver = get_web_driver(browser)
driver.get('https://www.baidu.com')

# 获取网页源代码并解析XML标签
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
xml_elements = soup.find_all('xml')

# 遍历XML标签，并封装每一个可操作的按钮为XPath
xpaths = []
for xml_element in xml_elements:
    buttons = xml_element.find_all('button')
    for button in buttons:
        if button.has_attr('id') and button.has_attr('name'):
            xpath = f"//button[@id='{button['id']}' and @name='{button['name']}']"
            xpaths.append(xpath)

# 打印所有的XPath
print(xpaths)

# 关闭浏览器
driver.quit()
