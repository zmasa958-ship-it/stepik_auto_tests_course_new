import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    # 1. Заполняем текстовые поля: имя, фамилия, email
    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys("Ivan")
    
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys("Petrov")
    
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("ivan.petrov@example.com")
    
    print("Текстовые поля заполнены")

    # 2. Создаем временный файл для загрузки
    # Получаем путь к текущей директории
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'bio.txt')
    
    # Создаем и записываем содержимое в файл
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("This is my short bio for the task.")
    
    print(f"Файл создан: {file_path}")

    # 3. Загружаем файл
    file_input = browser.find_element(By.CSS_SELECTOR, "#file")
    file_input.send_keys(file_path)
    print("Файл загружен")

    # 4. Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    print("Форма отправлена")

    # 5. Получаем результат из alert
    time.sleep(3)
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()

finally:
    # Удаляем созданный файл после завершения (опционально)
    try:
        os.remove(file_path)
        print(f"Временный файл удален: {file_path}")
    except:
        pass
    
    time.sleep(5)
    browser.quit()