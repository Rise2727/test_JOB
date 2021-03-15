from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
name = "Андрей"
email = "Andrey@gmail.com"

def registry(name, email):

    browser.get('https://timeweb.com/ru/services/hosting/?_ga=2.95324252.1788014157.1615540093-609408001.1615540093#hosting-optimo')
    # Ищем форму регистрации по классу и поля ввода имени и почты
    forma = browser.find_element_by_class_name("w560")
    yourNameField = forma.find_element_by_name("full_name")
    emailField = forma.find_element_by_name("email")
    # Вводим данные для регистрации
    yourNameField.send_keys(name)
    emailField.send_keys(email)
    # Жмем кнопку регистрации
    browser.find_element_by_class_name("js-send-hosting-form").click()
    # Ждем когда сайт прогрузятся
    time.sleep(5)


def parser():
    browser.get('https://hosting.timeweb.ru/')
    time.sleep(2)
    #поиск элемента хранящего время работы
    upTime = browser.find_elements(By.TAG_NAME, 'span')
    for textUpTime in upTime:
        if textUpTime.get_attribute("data-tooltip") == "Время непрерывной работы сервера без перезагрузки":
            #тут хранится информация о сроке работы сервера
            #print ("Время работы: ", textUpTime.text)
            break
    #абонентская плата и остаток дней
    dateoff = browser.find_elements(By.XPATH, "//div[@class='cpS-icon-n-info']")

    return [dateoff[0].text.replace("\n", ""), ("\n") , dateoff[1].text.replace("\n", ""), ("\n") , "Время работы сервера: ", textUpTime.text.replace("\n", ""), ("\n")]


def save_file(stroka):
    document = open("code.txt", "w")
    for text in stroka:
        document.write(text)


registry(name, email)
stroka = parser()
browser.quit()
print (stroka)
save_file(stroka)
#browser.close()
