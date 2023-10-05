from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver'ı başlat
chrome_options = Options()
chrome_options.add_argument("--headless")  # Arka planda çalıştırma
driver = webdriver.Chrome(options=chrome_options)

# Web sayfasını aç
URL = 'https://www.a101.com.tr/market/meyve-sebze/'
driver.get(URL)

urunList = []
fiyatList = []

# Fiyatı çekmek için XPath'i kullanın
for i in range(1, 49):
    isim = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, f'/html/body/section/section[3]/div[3]/div[3]/div/div[2]/div[2]/div/ul/li[{i}]/article/a/div/header/hgroup/h3'))
    )
    urunList.append(isim)

    fiyat = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, f'/html/body/section/section[3]/div[3]/div[3]/div/div[2]/div[2]/div/ul/li[{i}]/article/a/div/section[1]/span'))
    )
    fiyatList.append(fiyat)


# Fiyatı yazdırın
for i in range(len(urunList)):
    print(f"İsim: {urunList[i].text}")
    print(f"Fiyat: {fiyatList[i].text} TL")

# Tarayıcıyı kapat
driver.quit()