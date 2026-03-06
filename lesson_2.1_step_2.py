import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    # 1. Находим элемент-картинку (сундук) и берём из него значение атрибута "valuex"
    treasure_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = treasure_element.get_attribute("valuex")
    print(f"Значение x из атрибута: {x}")

    # 2. Вычисляем результат функции
    y = calc(x)
    print(f"Результат вычислений: {y}")

    # 3. Вводим ответ в текстовое поле
    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)

    # 4. Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    # 5. Выбираем radiobutton "Robots rule!"
    robots_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_radio.click()

    # 6. Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 7. Ждём результат и получаем код из alert
    time.sleep(5)
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()