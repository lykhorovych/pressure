from bluepy.btle import Peripheral, UUID
import time

# Підключення до Mi Band за MAC-адресою
def connect_to_band(mac_address):
    print("Підключення до пристрою...")
    band = Peripheral(mac_address)
    return band

# Зчитування рівня кисню в крові (якщо підтримується)
# def get_spo2(band):
#     try:
#         # Тут може бути UUID сервісу для вимірювання SpO2
#         # Замість цього потрібно знайти правильний UUID для вашої моделі
#         spo2_service = band.getServiceByUUID(UUID(0xXXXX))  # Замість 0xXXXX вкажіть правильний UUID
#         spo2_char = spo2_service.getCharacteristics()[0]
#         spo2_data = int.from_bytes(spo2_char.read(), byteorder='little')
#         print(f"Рівень кисню в крові: {spo2_data}%")
#     except Exception as e:
#         print(f"Не вдалося отримати дані про SpO2: {e}")

if __name__ == "__main__":
    mac_address = "90:EF:4A:42:C3:D7"  # Вкажіть MAC-адресу вашого Mi Band
    band = connect_to_band(mac_address)
    get_spo2(band)
