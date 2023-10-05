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
URL = 'https://www.migros.com.tr/meyve-sebze-c-2?sayfa=1&sirala=onerilenler'
driver.get(URL)

urunList = []
fiyatList = []

# Fiyatı çekmek için XPath'i kullanın
for i in range(1, 30):
    isim = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'/html/body/sm-root/div/main/sm-product/article/sm-list/div/div[4]/div[2]/div[4]/sm-list-page-item[{i}]/mat-card/div[1]/a'))
    )
    urunList.append(isim)

    fiyat = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f'/html/body/sm-root/div/main/sm-product/article/sm-list/div/div[4]/div[2]/div[4]/sm-list-page-item[{i}]/mat-card/div[2]/fe-product-price/div/div/span'))
    )
    fiyatList.append(fiyat)


# Fiyatı yazdırın
for i in range(len(urunList)):
    print(f"İsim: {urunList[i].text}")
    print(f"Fiyat: {fiyatList[i].text} TL")

# Tarayıcıyı kapat
driver.quit()
