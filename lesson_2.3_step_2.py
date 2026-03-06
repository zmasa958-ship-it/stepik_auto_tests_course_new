from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    
    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # На новой странице решить капчу
    # Находим значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    
    # Вычисляем результат
    y = calc(x)
    
    # Вводим ответ
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)
    
    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    
    # Получаем число из alert
    alert = browser.switch_to.alert
    alert_text = alert.text
    number = alert_text.split(": ")[-1]
    print(f"Полученное число: {number}")
    
    # Принимаем alert
    alert.accept()
    
    # Ждем немного перед закрытием
    time.sleep(2)
    
finally:
    # Закрываем браузер
    browser.quit()