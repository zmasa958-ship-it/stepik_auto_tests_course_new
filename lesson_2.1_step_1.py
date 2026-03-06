import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Небольшая пауза для загрузки страницы
    time.sleep(1)
    
    # Считываем значение x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    print(f"Значение x: {x}")
    
    # Вычисляем результат
    y = calc(x)
    print(f"Результат вычислений: {y}")
    
    # Вводим ответ в текстовое поле
    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)
    
    # Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()
    
    # Выбираем radiobutton "Robots rule!"
    robots_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_radio.click()
    
    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # Ждем результат
    time.sleep(5)
    
    # Получаем alert с проверочным кодом
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()
    
finally:
    time.sleep(5)
    browser.quit()