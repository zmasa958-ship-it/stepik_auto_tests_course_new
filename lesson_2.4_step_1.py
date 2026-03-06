from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу (УБЕДИТЕСЬ, ЧТО URL ВЕРНЫЙ!)
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html") # Проверьте этот адрес

    # 1. Дождаться, когда цена станет $100 (ожидание до 12 секунд)
    #    Используем text_to_be_present_in_element для проверки текста элемента
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        # Возможно, на странице другой ID, например "price_value"
    )

    # 2. Нажать кнопку "Book"
    book_button = browser.find_element(By.ID, "book") # ID кнопки может быть другим
    book_button.click()

    # 3. Решить математическую задачу (на новой странице/этапе)
    # Найти значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Вычислить результат
    y = calc(x)

    # Ввести ответ
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Нажать кнопку "Submit" / "Отправить"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']") # Селектор может отличаться
    submit_button.click()

    # Получить число из alert и вывести его
    alert = browser.switch_to.alert
    alert_text = alert.text
    number = alert_text.split(": ")[-1]
    print(f"Полученное число: {number}")
    alert.accept()

    time.sleep(2)

finally:
    browser.quit()