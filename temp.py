from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
link = 'https://josaa.nic.in/class12/Class12th21.htm'

Value = 22608677


def enterRoll(driver, Value):
    input = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[1]/td[2]/input')
    input.send_keys(Value)

def enterSchoolCode(driver):
    input = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[2]/td[2]/input')
    input.send_keys(66262)

def submit(driver):
    input = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[3]/td/input[1]')
    input.send_keys(Keys.RETURN)

def resultScore(driver):
    result = 0;
    for i in range(2,7):
        result += int(driver.find_element_by_xpath(f'/html/body/div/div/center/table/tbody/tr[{i}]/td[5]/font').text)
    return result

def displayResult(driver,roll_no, name, marks):
    fields=[roll_no, name, marks]
    with open('scores.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

name = ''

def getName(driver):
    global name
    name = driver.find_element_by_xpath('/html/body/div/table[1]/tbody/tr[2]/td[2]').text

def checkAnother(driver):
    pass

def startAll():
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')

    driver.get(link)

    global Value

    print("entering Roll")
    enterRoll(driver,Value)

    print("entering School Code")
    enterSchoolCode(driver)

    print("Submitting...")
    submit(driver)

    time.sleep(1)

    print("summing up scores....")
    Result = resultScore(driver);

    print("getting name...")
    getName(driver);

    print("Adding to DB...")
    displayResult(driver,Value, name, Result)

    Value += 1

    # driver.execute_script("window.open('"+link+"', '__blank__');")
    driver.quit()
    print('next')
    print("left : ", 22608956 - Value)



while (Value <= 22608956):
    startAll();
