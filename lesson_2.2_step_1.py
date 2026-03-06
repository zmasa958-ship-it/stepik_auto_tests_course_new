from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    # 1. Находим элементы с числами и получаем их текст
    num1_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    num2_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    
    # Преобразуем текст в целые числа для сложения
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)
    print(f"Найдены числа: {num1} и {num2}")

    # 2. Вычисляем сумму
    sum_result = num1 + num2
    print(f"Сумма: {sum_result}")

    # 3. Работаем с выпадающим списком (селектом)
    # Находим сам элемент select
    select_element = browser.find_element(By.CSS_SELECTOR, "#dropdown")
    # Создаём объект Select для удобной работы
    select = Select(select_element)
    
    # Важно! Значение для выбора должно быть строкой, поэтому преобразуем сумму в str
    select.select_by_value(str(sum_result))
    print(f"Выбрано значение: {sum_result}")

    # 4. Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 5. Получаем результат из alert
    time.sleep(3)
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()