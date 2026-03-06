# lesson_2.2_step_2.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Вычисляем функцию
    y = calc(x)

    # Находим поле ввода
    input_field = browser.find_element(By.ID, "answer")

    # Скроллим страницу к полю ввода
    browser.execute_script("arguments[0].scrollIntoView(true);", input_field)

    # Вводим ответ
    input_field.send_keys(y)

    # Отмечаем checkbox
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбираем radiobutton
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # Даем время увидеть результат
    time.sleep(5)
    browser.quit()