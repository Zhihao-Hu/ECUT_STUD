from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import requests

def isConnected():#判断网络是否连接函数
    try:
        html = requests.get("https://www.baidu.com",timeout=2)
        return 1
    except:
        return 0

def login():#连接校园网函数

    driver = webdriver.Chrome()#初始化webdrive
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10, 0.5)
    driver.get("http://172.21.255.105")#获取网页
    wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div[2]/div/a/img")))
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[3]/form/input[3]').send_keys(学号)#括号内填学号
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[3]/form/input[4]').send_keys('密码')#单引号内填密码
    s = driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[3]/select')
    Select(s).select_by_value('@cmcc')#如果你是移动校园网 那不用改；联通将cmcc改为unicom；电信将cmcc改为telecom
    time.sleep(2)
    shit = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[3]/form/input[2]')
    driver.execute_script('arguments[0].click()',shit)

flag = isConnected()#判断校园网是否连接
if flag == 0:
    print('网络异常')
    print('正在光速速连接中',end="")
    count=0
    while count<10:
        time.sleep(0.3)
        print("*",end="")
        count=count+1
    print("")
    login()



judge = isConnected()#判断校园网是否连接成功
if judge == 1:
    print("网络连接成功！！！")
