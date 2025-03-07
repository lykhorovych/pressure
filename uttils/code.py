from pyband import PyBand
import time

# Підключення до Mi Band
def connect_band():
    band = PyBand()
    band.scan()
    devices = band.get_devices()

    if devices:
        print("Доступні пристрої:")
        for i, device in enumerate(devices):
            print(f"{i + 1}: {device}")
        # Підключаємось до першого пристрою
        selected_device = devices[0]
        band.connect(selected_device)
        return band
    return None

# Включення екрану
def turn_on_screen(band):
    band.set_screen_on(True)
    print("Екран включено.")

# Вимкнення екрану
def turn_off_screen(band):
    band.set_screen_on(False)
    print("Екран вимкнено.")

# Відображення повідомлення
def display_message(band, message):
    band.show_message(message)
    print(f"Повідомлення відображено: {message}")

# Відображення часу
def display_time(band):
    band.show_time()
    print("Час відображено на екрані.")

# Отримання пульсу
def get_heart_rate(band):
    heart_rate = band.get_heart_rate()
    print(f"Пульс: {heart_rate} bpm")

# Отримання даних про сон
def get_sleep_data(band):
    sleep_data = band.get_sleep_data()
    print("Дані про сон:")
    for entry in sleep_data:
        print(f"Дата: {entry.date}, Тривалість: {entry.duration} хв, Стан: {entry.state}")

# Отримуємо кроки
def get_steps(band):
    steps = band.get_steps()
    print(f"Кроки: {steps}")

# Скидання кроків
def reset_steps(band):
    band.reset_steps()
    print("Статистика кроків скинута.")
