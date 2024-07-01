from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import locale
from datetime import datetime, timedelta
import pyperclip
import os
import mss
from time import sleep


class TestSENARYOSU1():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()

   def test_BasariliGirisKontrolu(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
      username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
      username.send_keys("koc1eray@gmail.com")
      password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
      password.send_keys("Passw0rd!")
      self.driver.execute_script("window.scrollTo(0, 500)")
      WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
      loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
      loginbutton.click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Giriş başarılı."
   
   def test_EpostaveyaSifreGirilmediginde(self):
      eposta = ["", "aaa@gmail.com", ""]
      sifre = ["123456", "", ""]
      i = 0
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
      username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
      password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
      while i < 3:
         username.send_keys(eposta[i])
         password.send_keys(sifre[i])
         self.driver.execute_script("window.scrollTo(0, 80)")
         sleep(5)
         loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
         try:
            loginbutton.click()
            i = 20
         except:
            i += 1
         username.clear()
         password.clear()
      assert i == 3

   def test_EpostaveyaSifreHataliGirildiginde(self):
      eposta = ["abc@gmail.com", "koc1eray@gmail.com", "abc@gmail.com"]
      sifre = ["Passw0rd!", "12378", "asckjabcshab"]
      i = 0
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
      username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
      password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
      loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
      while i < 3:
         username.send_keys(eposta[i])
         password.send_keys(sifre[i])
         WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
         loginbutton.click()
         WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
         if self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Geçersiz e-posta veya şifre.":
            i += 1
         else:
            i = 20
         username.clear()
         password.clear()
         sleep(5)
      assert i == 3


# class TestSENARYOSU2():
#    def setup_method(self, method):
#     chromedriver_autoinstaller.install()
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_extension("buster.crx")
#     self.driver = webdriver.Chrome(options=chrome_options)
#     self.driver.get("https://tobeto.com/sifremi-unuttum")
#     self.driver.maximize_window()
  
#    def teardown_method(self, method):
#     self.driver.quit()

#    def test_BasariliKayitOlKontrolu(self):
#       WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/input[1]")))



class TestSENARYOSU3():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/sifremi-unuttum")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()

   def test_SifreSifirlamaEpostaGonderme(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/input[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/input[1]").send_keys("koc1eray@gmail.com")
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin."
   
   def test_SifreSifirlamaDurumundaHataliEpostaGirilmesi(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/input[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/input[1]").send_keys("geçersiz@gmail")
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Girdiğiniz e-posta geçersizdir."


class TestSENARYOSU4():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()

   def test_BasariliGirisKontrolu(self):
      WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@id='exw-launcher-frame']")))
      littlechatbutton = self.driver.find_element(By.XPATH, "/html/body/div/div/button")
      littlechatbutton.click()
      self.driver.switch_to.default_content()
      WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='exw-conversation-container-frame']")))
      minimize_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "svg.exw-minimize-button")))
      minimize_button.click()
      try:
         self.driver.switch_to.default_content()
         WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@id='exw-launcher-frame']")))
         littlechatbutton.click()
         assert True
      except:
         assert False
   
   def test_ChatBotMesajBolumuKontrol(self):
      WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@id='exw-launcher-frame']")))
      self.driver.find_element(By.XPATH, "/html/body/div/div/button").click()
      self.driver.switch_to.default_content()
      WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='exw-conversation-container-frame']")))
      WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[2]/div[2]/input")))
      self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[2]/div[2]/input").send_keys("Mehmet Aslantaş", Keys.ENTER)
      WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]")))
      self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]").click()
      sleep(10)
      assert self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[5]/div[2]/div/div/div/div/p").text == "Tobeto’da ihtiyaçların ve kaynaklarına göre öğrenim yolculuğunu sen tasarlarsın. Tobeto değerlendirme araçlarıyla kendini test edebilirsin."

   def test_ChatBotMesajBolumunuSonlandirma(self):
      WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@id='exw-launcher-frame']")))
      self.driver.find_element(By.XPATH, "/html/body/div/div/button").click()
      self.driver.switch_to.default_content()
      WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='exw-conversation-container-frame']")))
      WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#exw-conversation-frame-body > div > div > div > div.exw-header-and-loading > div > div.exw-header-buttons > svg.exw-end-session-button.header-button")))
      self.driver.find_element(By.CSS_SELECTOR, "#exw-conversation-frame-body > div > div > div > div.exw-header-and-loading > div > div.exw-header-buttons > svg.exw-end-session-button.header-button").click()
      WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div[3]/div/button[1]")))
      self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div[3]/div/button[1]").click()
      WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div/form/textarea")))
      self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div/form/textarea").send_keys("Merhaba")
      sleep(1)
      self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div/form/button").click()
      WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div/div/h3")))
      assert self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div/div/h3").text == "Geri bildiriminiz için teşekkürler!"

   
   def test_EmojiKontrolu(self):
      WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@id='exw-launcher-frame']")))
      self.driver.find_element(By.XPATH, "/html/body/div/div/button").click()
      self.driver.switch_to.default_content()
      WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='exw-conversation-container-frame']")))
      EmojiButton = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[3]/form/div/a")))
      EmojiButton.click()
      shadow_host = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[3]/div[1]/div/emoji-picker")))
      script = '''
        const shadowRoot = arguments[0].shadowRoot;
        const emoji = shadowRoot.querySelector('#skintone-button');
        emoji.click();'''
      self.driver.execute_script(script, shadow_host)
      assert True

   def test_DosyaKontrolu(self):
      WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@id='exw-launcher-frame']")))
      self.driver.find_element(By.XPATH, "/html/body/div/div/button").click()
      self.driver.switch_to.default_content()
      WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='exw-conversation-container-frame']")))
      attach = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[3]/form/div/button")))
      attach.click()
      button = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[3]/div[2]/div[2]/button")))
      assert button.text == "Dosya Seçiniz"



class TestSENARYOSU5():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()

   def test_FiltresizTumEgitimlerinTakvimdeGosterilmesi(self):
      clndrbtn = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/div[2]/div")))
      clndrbtn.click()
      checkbox = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[1]/input")))
      checkbox.click()
      self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[2]/input").click()
      self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[3]/input").click()
      self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[4]/input").click()
      sleep(1)
      project_directory = os.path.dirname(os.path.abspath(__file__))
      screenshots_directory = os.path.join(project_directory, 'Screenshot')
      screenshot_path = os.path.join(screenshots_directory, 'test_EgitimAramaFiltresininKontrolu.png')
      self.driver.save_screenshot(screenshot_path)
      assert True

   def test_EgitimAramaFiltresininKontrolu(self):
      clndrbtn = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/div[2]/div")))
      clndrbtn.click()
      checkbox = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[1]/input")))
      checkbox.click()
      self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[2]/input").click()
      self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[3]/input").click()
      self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[4]/input").click()
      sleep(1)
      project_directory = os.path.dirname(os.path.abspath(__file__))
      screenshots_directory = os.path.join(project_directory, 'Screenshot')
      screenshot_path = os.path.join(screenshots_directory, 'test_EgitimAramaFiltresininKontrolu.png')
      self.driver.save_screenshot(screenshot_path)
      assert True

   def test_EgitmenAramaFiltresininKontrolu(self):
      clndrbtn = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/div[2]/div")))
      clndrbtn.click()
      checkbox = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[1]/input")))
      checkbox.click()
      self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[2]/input").click()
      self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[3]/input").click()
      self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[4]/input").click()
      inputfilter = WebDriverWait(self.driver, 35).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-select-2-input"]')))
      inputfilter.send_keys("Gürk", Keys.TAB)
      project_directory = os.path.dirname(os.path.abspath(__file__))
      screenshots_directory = os.path.join(project_directory, 'Screenshot')
      screenshot_path = os.path.join(screenshots_directory, 'test_EgitmenAramaFiltresininKontrolu.png')
      self.driver.save_screenshot(screenshot_path)
      assert True

   def test_EgitmenVeEgitimAramaBirlikteKontrol(self):
      clndrbtn = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/div[2]/div")))
      clndrbtn.click()
      checkbox = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[1]/input")))
      checkbox.click()
      self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[2]/input").click()
      self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[3]/input").click()
      self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/span[4]/input").click()
      inputfilter = WebDriverWait(self.driver, 35).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-select-2-input"]')))
      inputfilter.send_keys("Gürk", Keys.TAB)
      EgitimInput = WebDriverWait(self.driver, 35).until(EC.presence_of_element_located((By.ID, "search-event")))
      EgitimInput.send_keys("Java")
      project_directory = os.path.dirname(os.path.abspath(__file__))
      screenshots_directory = os.path.join(project_directory, 'Screenshot')
      screenshot_path = os.path.join(screenshots_directory, 'test_EgitmenVeEgitimAramaBirlikteKontrol.png')
      self.driver.save_screenshot(screenshot_path)
      assert True

   def test_TarihYonlendirmeButonlarininKontrolu(self):
      clndrbtn = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/div[2]/div")))
      clndrbtn.click()
      TodayButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@class='fc-today-button fc-button fc-button-primary']")))
      TodayButton.click()
      locale.setlocale(locale.LC_TIME, 'turkish')
      now = datetime.now()
      current_month = now.strftime('%B')
      previous_month_var = now.replace(day=1) - timedelta(days=1)
      previous_month = previous_month_var.strftime('%B')
      CheckText = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, "fc-dom-1"))).text
      assert CheckText == f"{current_month} 2024"
      NextButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@class='fc-next-button fc-button fc-button-primary']")))
      PreviousButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@class='fc-prev-button fc-button fc-button-primary']")))
      PreviousButton.click()
      CheckText = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, "fc-dom-1"))).text
      assert CheckText == f"{previous_month} 2024"
      for i in range(2):
         NextButton.click()
      if now.month == 12:
         next_month_var = now.replace(year=now.year + 1, month=1, day=1)
      else:
         next_month_var = now.replace(month=now.month + 1, day=1)
      next_month = next_month_var.strftime('%B')
      CheckText = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, "fc-dom-1"))).text
      assert CheckText == f"{next_month} 2024"
      self.driver.find_element(By.XPATH, "//button[@title='Ay']").click()
      project_directory = os.path.dirname(os.path.abspath(__file__))
      screenshots_directory = os.path.join(project_directory, 'Screenshot')
      screenshot_path = os.path.join(screenshots_directory, 'CalendarMonth.png')
      self.driver.save_screenshot(screenshot_path)
      self.driver.find_element(By.XPATH, "//button[@title='Hafta']").click()
      screenshot_path = os.path.join(screenshots_directory, 'CalendarWeek.png')
      self.driver.save_screenshot(screenshot_path)
      self.driver.find_element(By.XPATH, "//button[@title='Gün']").click()
      screenshot_path = os.path.join(screenshots_directory, 'CalendarDay.png')
      self.driver.save_screenshot(screenshot_path)

   def test_TakvimPopUpninKapatilmasiKontrolu(self):
      clndrbtn = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/div[2]/div")))
      clndrbtn.click()
      CloseButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn-close btn-close-white']")))
      CloseButton.click()
      CheckText = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[2]/span"))).text
      assert CheckText == "Hoşgeldiniz"


class TestSENARYOSU6():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()
  
   def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("lotofloveb4n@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          self.driver.execute_script("window.scrollTo(0, 500)")
          WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
          loginbutton = self.driver.find_element(By.XPATH, "//button[@type='submit']")
          loginbutton.click()
          func(self)
      return login
   
   @succesful_login_decorator
   def test_TumEgitimlerinGoruntulenmesi(self):
      WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.XPATH, "//p[@class='tobeto-slogan']")))
      assert self.driver.current_url == "https://tobeto.com/platform"

   @succesful_login_decorator
   def test_HosgeldinizPaneliKontrolu(self):
      CheckText = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='apply-tab-pane']/div/div/div/div[1]/div[1]/span")))
      assert CheckText.text == "İstanbul Kodluyor"
      self.driver.find_element(By.XPATH, "//button[@id='lessons-tab']").click()
      ShowMoreButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/section[2]/div/div/div[3]/div/div[2]/div/div/div[2]")))
      ShowMoreButton.click()
      HomePage = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/nav/div[1]/a")))
      HomePage.click()
      News = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@id='notification-tab']")))
      News.click()
      AnnouncementText = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/section[2]/div/div/div[3]/div/div[3]/div/div[2]/div/div[1]/div/span[1]"))).text
      assert AnnouncementText == "Duyuru"
      self.driver.find_element(By.XPATH, "//button[@id='mySurvey-tab']").click()
      CheckText = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='mySurvey-tab-pane']/div/div/p"))).text
      assert CheckText == "Atanmış herhangi bir anketiniz bulunmamaktadır"

   @succesful_login_decorator
   def test_SinavlarimButonunuKontrolu(self):
      Cart = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/section[3]/div/div/div[2]/div/div[1]/span[1]")))
      Cart.click()
      ViweReportButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary mt-8 ms-auto me-auto']")))
      ViweReportButton.click()
      CloseButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary mt-8 ms-auto me-auto']")))
      CloseButton.click()
      assert self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[1]/section[3]/div/div/div[2]/div/div[1]/span[1]").text == "Herkes İçin Kodlama 5B Değerlendirme Sınavı"

   @succesful_login_decorator
   def test_KisiselAlanKontrolu(self):
      WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/section[4]/div/div/div[1]/div/button")))
      Buttons = self.driver.find_elements(By.XPATH, "//button[@class='btn btn-primary w-100 ']")
      Buttons[0].click()
      WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/label")))
      assert self.driver.current_url == "https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim"
      HomePage = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/nav/div[1]/a")))
      HomePage.click()
      WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/section[4]/div/div/div[1]/div/button")))
      Buttons = self.driver.find_elements(By.XPATH, "//button[@class='btn btn-primary w-100 ']")
      Buttons[1].click()
      WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section[2]/div/div/div[1]/div/a")))
      assert self.driver.current_url == "https://tobeto.com/degerlendirmeler"
      HomePage = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/nav/div[1]/a")))
      HomePage.click()
      var = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/section[4]/div/div/div[3]/div/button")))
      var.click()
      WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div/div/div[2]/div[2]/div/div/p")))
      assert self.driver.current_url == "https://tobeto.com/platform-katalog"



class TestSENARYOSU7():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()
  
   def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("lotofloveb4n@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          self.driver.execute_script("window.scrollTo(0, 500)")
          WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
          loginbutton = self.driver.find_element(By.XPATH, "//button[@type='submit']")
          loginbutton.click()
          func(self)
      return login
   
   @succesful_login_decorator
   def test_EgitimlerimPanelineYonlendirme(self):
      EducationButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@id='lessons-tab']")))
      EducationButton.click()
      self.driver.execute_script("window.scrollTo(0, 700)")
      project_directory = os.path.dirname(os.path.abspath(__file__))
      screenshots_directory = os.path.join(project_directory, 'Screenshot')
      screenshot_path = os.path.join(screenshots_directory, 'ListFourOfEducations.png')
      self.driver.save_screenshot(screenshot_path)
      ShowMoreButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/section[2]/div/div/div[3]/div/div[2]/div/div/div[2]")))
      ShowMoreButton.click()
      sleep(0.5)
      self.driver.execute_script("window.scrollTo(0, 350)")
      screenshot_path = os.path.join(screenshots_directory, 'ListAllEducations.png')
      self.driver.save_screenshot(screenshot_path)
      sleep(4)
      assert self.driver.current_url == "https://tobeto.com/egitimlerim"

   @succesful_login_decorator
   def test_KullaniciyaAtananEgitimIceriklerininKontrolu(self):
      EducationButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@id='lessons-tab']")))
      EducationButton.click()
      VideoButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='all-lessons-tab-pane']/div/div[2]/div/div[2]/button")))
      VideoButton.click()
      CountText = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='dynamicContent']/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/span[2]/span")))
      LikeCount = int(CountText.text)
      self.driver.find_element(By.XPATH, "//*[@id='main-content']").click()
      sleep(1)
      assert LikeCount + 1 == int(self.driver.find_element(By.XPATH, "//*[@id='dynamicContent']/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div/span[2]/span").text)
      self.driver.find_element(By.XPATH, "//*[@id='dynamicContent']/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[4]/div/span").click()
      CheckText = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='wrapper-content']/div[2]/div/div/p")))
      assert CheckText.text == "Favorilere ekleme işlemin başarıyla gerçekleşti."
      project_directory = os.path.dirname(os.path.abspath(__file__))
      screenshots_directory = os.path.join(project_directory, 'Screenshot')
      screenshot_path = os.path.join(screenshots_directory, 'BothYellowAndRed.png')
      self.driver.save_screenshot(screenshot_path)
      self.driver.find_element(By.XPATH, "//*[@id='rc-tabs-0-tab-content']/div").click()
      assert self.driver.find_element(By.XPATH, "//*[@id='directory-18121']/div[1]/div[2]/span").text == "Video - 3 dk"
      self.driver.find_element(By.XPATH, "//*[@id='rc-tabs-0-tab-about']/div/span").click()
      CheckText = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='rc-tabs-0-panel-about']/div/div[2]/div[1]/strong")))
      assert CheckText.text == "Tahmini Süre"
      self.driver.find_element(By.XPATH, "//*[@id='rc-tabs-0-tab-content']/div").click()
      DetailButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='activity-unit-detail']/div/div[2]/div/div/div[2]/button")))
      DetailButton.click()
      GetToEducationPage = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]")))
      GetToEducationPage.click()
      CheckText = self.driver.find_element(By.XPATH, "//*[@id='activity-unit-detail']/div/div[1]/div[2]").text
      assert CheckText == "Video - 3 dk"
      self.driver.find_element(By.XPATH, "//*[@id='activity-unit-detail']/div/div[2]/div/div/div[2]/button").click()
      XButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]")))
      XButton.click()
      CheckText = self.driver.find_element(By.XPATH, "//*[@id='activity-unit-detail']/div/div[1]/div[2]").text
      assert CheckText == "Video - 3 dk"
      

   @succesful_login_decorator
   def test_EgitimlerimSayfasindaAramaYapilmasi(self):
      EducationButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@id='lessons-tab']")))
      EducationButton.click()
      ShowMoreButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[1]/section[2]/div/div/div[3]/div/div[2]/div/div/div[2]")))
      ShowMoreButton.click()
      SearchBar = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='search']")))
      SearchBar.send_keys("Dr. Ecmel")
      self.driver.execute_script("window.scrollTo(0, 200)")
      project_directory = os.path.dirname(os.path.abspath(__file__))
      screenshots_directory = os.path.join(project_directory, 'Screenshot')
      screenshot_path = os.path.join(screenshots_directory, 'SearchBar.png')
      self.driver.save_screenshot(screenshot_path)
      SearchBar.send_keys(Keys.CONTROL, "a")
      SearchBar.send_keys(Keys.BACKSPACE)
      inputs = self.driver.find_elements(By.XPATH, "//input[@class='select__input']")
      inputs[0].send_keys("İst", Keys.TAB)
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]").text == "İstanbul Kodluyor"
      Datas = ["Adına Göre (A-Z)", "Adına Göre (Z-A)", "Tarihe Göre (Y-E)", "Tarihe Göre (E-Y)"]
      for data in Datas:
         inputs[1].send_keys(data, Keys.TAB)
         sleep(1.5)
         screenshot_path = os.path.join(screenshots_directory, f'{data}.png')
         self.driver.save_screenshot(screenshot_path)



class TestSENARYOSU8():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()
  
   def succesful_login_decorator(func):
     def login(self):
         WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
         username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
         username.send_keys("lotofloveb4n@gmail.com")
         password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
         password.send_keys("Passw0rd!")
         self.driver.execute_script("window.scrollTo(0, 500)")
         WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
         loginbutton = self.driver.find_element(By.XPATH, "//button[@type='submit']")
         loginbutton.click()
         func(self)
     return login
   
   @succesful_login_decorator
   def test_DuyuruVeHaberlerimKisminaErişimKontrolu(self):
      AnnounceButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@id='notification-tab']")))
      AnnounceButton.click()
      CheckText = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='notification-tab-pane']/div/div[1]/div/div[1]/span")))
      assert CheckText.text == "Mentor Oturumları Hk."

   @succesful_login_decorator
   def test_DuyuruVeHaberlerimKismiFiltrelemeIslemlerininKontrolu(self):
      AnnounceButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@id='notification-tab']")))
      AnnounceButton.click()
      ShowMoreButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='notification-tab-pane']/div[1]/div[4]")))
      ShowMoreButton.click()
      SearchBar = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='search']")))
      SearchBar.send_keys("Ocak Ayı Tercih")
      WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[2]/div/div/div[1]/span")))
      sleep(1)
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div[2]/div/div/div[1]/span").text == "Ocak Ayı Tercih Formu Bilgilendirmesi"
      SearchBar.clear()
      SearchBar.send_keys("Ocak Ayı Topları")
      sleep(1)
      WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[2]/div/p")))
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div[2]/div/p").text == "Bir duyuru bulunmamaktadır."
      SearchBar.send_keys(Keys.CONTROL, "a")
      SearchBar.send_keys(Keys.BACKSPACE)
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[2]/div[1]/div[1]/div[2]/button[1]").click()
      sleep(0.2)
      News = self.driver.find_element(By.XPATH, "//*[@id='typeNews']")
      News.click()
      CheckText = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[2]/div[2]/div[1]/p[1]")))
      assert CheckText.text == "Bir duyuru bulunmamaktadır."
      News.click()
      self.driver.find_element(By.XPATH, "//*[@id='typeAnnouncement']").click()
      CheckText = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]")))
      assert CheckText.text == "Mentor Oturumları Hk."



class TestSENARYOSU9():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()
  
   def succesful_login_decorator(func):
     def login(self):
         WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
         username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
         username.send_keys("koc1eray@gmail.com")
         password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
         password.send_keys("Passw0rd!")
         self.driver.execute_script("window.scrollTo(0, 500)")
         WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
         loginbutton = self.driver.find_element(By.XPATH, "//button[@type='submit']")
         loginbutton.click()
         func(self)
     return login
   
   @succesful_login_decorator
   def test_ProfilBilgileriSayfasinaGecis(self):
      XButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/div[1]/div[1]/div[1]/button[1]")))
      XButton.click()
      svg = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/nav[1]/div[1]/button[1]")))
      svg.click()
      ProfilimButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='offcanvasExample']/div[2]/div[1]/ul[1]/li[1]/a[3]")))
      ProfilimButton.click()
      WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")))
      assert self.driver.current_url == "https://tobeto.com/profilim"

   @succesful_login_decorator
   def test_ProfilBilgileriSayfasindaDuzenlemeIslemi(self):
      XButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/div[1]/div[1]/div[1]/button[1]")))
      XButton.click()
      svg = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/nav[1]/div[1]/button[1]")))
      svg.click()
      ProfilimButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='offcanvasExample']/div[2]/div[1]/ul[1]/li[1]/a[3]")))
      ProfilimButton.click()
      ShareButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='dropdown-basic']")))
      ShareButton.click()
      SwitchButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")))
      SwitchButton.click()
      sleep(0.6)
      project_directory = os.path.dirname(os.path.abspath(__file__))
      screenshots_directory = os.path.join(project_directory, 'Screenshot')
      screenshot_path = os.path.join(screenshots_directory, 'SwitchButton1.png')
      self.driver.save_screenshot(screenshot_path)
      SwitchButton.click()
      sleep(0.6)
      screenshot_path = os.path.join(screenshots_directory, 'SwitchButton2.png')
      self.driver.save_screenshot(screenshot_path)
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/i[1]").click()
      link = pyperclip.paste()
      CheckText = "https://tobeto.com/profiller"
      i = 0
      while i < len(CheckText):
         assert CheckText[i] == link[i]
         i += 1
   
   @succesful_login_decorator
   def test_SertifikaBolumununKontrolu(self):
      XButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/div[1]/div[1]/div[1]/button[1]")))
      XButton.click()
      svg = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/nav[1]/div[1]/button[1]")))
      svg.click()
      ProfilimButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='offcanvasExample']/div[2]/div[1]/ul[1]/li[1]/a[3]")))
      ProfilimButton.click()
      DownloadDiv = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div/div/div[2]/div/div[5]/div/div[2]/div/div[2]")))
      self.driver.execute_script("window.scrollTo(0, 1000)")
      DownloadDiv.click()
      sleep(2)
      output_dir = "Screenshot"
      output_filename = "SertifikaDownload.png"
      output_path = os.path.join(output_dir, output_filename)
      with mss.mss() as sct:
         screenshot = sct.shot(output=output_path)


class TestSENARYOSU10():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()
  
   def succesful_login_decorator(func):
     def login(self):
         WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
         username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
         username.send_keys("koc1eray@gmail.com")
         password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
         password.send_keys("Passw0rd!")
         self.driver.execute_script("window.scrollTo(0, 500)")
         xpath = "//*[@id='exaironWebchat']/div/div/div"
         script = """
         var element = document.evaluate(arguments[0], document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
         if (element) element.parentNode.removeChild(element);
         """
         self.driver.execute_script(script, xpath)
         WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
         loginbutton = self.driver.find_element(By.XPATH, "//button[@type='submit']")
         loginbutton.click()
         func(self)
     return login

   @succesful_login_decorator
   def test_RaporGoruntulemeKontrol(self):
      XButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/div[1]/div[1]/div[1]/button[1]")))
      XButton.click()
      svg = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/nav[1]/div[1]/button[1]")))
      svg.click()
      DegerlendirmelerButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='offcanvasExample']/div[2]/div[1]/ul[1]/li[1]/a[2]")))
      DegerlendirmelerButton.click()
      ViewReportButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[2]/div[1]/div[1]/div[1]/div[1]/a[1]")))
      ViewReportButton.click()
      CheckText = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/div[1]/p[1]")))
      assert CheckText.text == "Analiz Raporum"

   
   @succesful_login_decorator
   def test_CoktanSecmeliDerslerinRaporGoruntulenmesı(self):
      XButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/div[1]/div[1]/div[1]/button[1]")))
      XButton.click()
      svg = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/nav[1]/div[1]/button[1]")))
      svg.click()
      DegerlendirmelerButton = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='offcanvasExample']/div[2]/div[1]/ul[1]/li[1]/a[2]")))
      DegerlendirmelerButton.click()
      sleep(3)
      self.driver.execute_script("window.scrollTo(0, 700)")
      ViewReport = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section[2]/div/div/div[4]/div/div[4]/button")))
      ViewReport.click()
      CheckTest = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div/div/div[1]/span")))
      assert CheckTest.text == "Microsoft SQL Server"
      



class TestSENARYOSU11():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()
  
   def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("koc1eray@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          self.driver.execute_script("window.scrollTo(0, 500)")
          WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
          loginbutton.click()
          func(self)
      return login
   
   @succesful_login_decorator
   def test_YetkinlikDetaylarinaAitAltBasliklarinAcilirPenceredeGoruntulenmesi(self):
      Button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[2]/div[1]/button[1]")))
      Button.click()
      ViewReport = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[2]/div[1]/div[1]/div[1]/div[1]/a[1]")))
      ViewReport.click()
      AccordionButton = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='heading8']/button[1]")))
      AccordionButton.click()
      CheckText = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='collapse8']/div[1]/div[1]/p[1]/span[1]")))
      assert CheckText.text == "Tobeto ‘İşte Başarı Modeli’nin son yetkinliği yeni dünya ile ilgilidir. Bu yetkinlik, diğer yedi yetkinlikten farklı olarak, yeni dünya ile ilgili farkındalık yaratmak ve herkesin kendisini olabildiğince buna hazırlaması konusunda yönlendirici olması için modele eklenmiştir. Zira içinde bulunduğumuz zamanlar önemli bir geçiş sürecine işaret etmektedir. Dijital teknolojilerle birlikte yaşanan dönüşümler hayatın her alanını yeninden şekillendirmektedir. "
      
   @succesful_login_decorator
   def test_AnalizRaporuGoruntuleme(self):
      Button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[2]/div[1]/button[1]")))
      Button.click()
      ViewReport = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[2]/div[1]/div[1]/div[1]/div[1]/a[1]")))
      ViewReport.click()
      Canvas = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/div/div[2]/div/div[1]/canvas")))
      assert True == Canvas.is_displayed()

      


class TestSENARYOSU12():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()

   def get_shadow_root(element, self):
    return self.driver.execute_script('return arguments[0].shadowRoot', element)
  
   def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("koc1eray@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          self.driver.execute_script("window.scrollTo(0, 500)")
          WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
          loginbutton.click()
          func(self)
      return login
   
   @succesful_login_decorator
   def test_profil_basliklarinin_kontrolu(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/label")))
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/label").text == "Adınız*"
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]")))
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]").text == "Kurum Adı*"
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[3]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[3]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]")))
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]").text == "Eğitim Durumu*"
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[4]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[4]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/label[1]")))
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/label[1]").text == "Yetkinlik"
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[5]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[5]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/label[1]")))
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/label[1]").text == "Sertifika Adı*"

      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[6]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[6]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]")))
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]").text == "Kulüp veya Topluluk Adı*"

      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[7]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[7]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]")))
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]").text == "Proje veya Ödül Adı*"

      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[8]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[8]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]")))
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]").text == "Kaydet"

      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[9]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[9]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/button[1]")))
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/button[1]").text == "Kaydet"

      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[10]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[10]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]")))
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/label[1]").text == "Eski Şifre*"
class TestSENARYOSU13():
  def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("koc1eray@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          self.driver.execute_script("window.scrollTo(0, 500)")
          WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
          loginbutton.click()
          func(self)
      return login
  
  @succesful_login_decorator
  def test_kisiselbilgileringuncellenmesi(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "name")))
     self.driver.find_element(By.NAME, "name").send_keys("Eray")
     self.driver.find_element(By.NAME, "surname").send_keys("Koç")
     self.driver.find_element(By.ID, "phoneNumber").send_keys("+902222222222")
     self.driver.find_element(By.NAME, "birthday").send_keys("2003-01-14")
     gender = self.driver.find_element(By.ID, "react-select-2-input")
     gender.send_keys("Erkek")
     gender.send_keys(Keys.ENTER)
     self.driver.find_element(By.XPATH, "//*[@id='react-select-3-input']").send_keys("T", Keys.ENTER)
     self.driver.find_element(By.ID, "react-select-4-input").send_keys("Yok")
     git = self.driver.find_element(By.NAME, "githubAddress")
     git.send_keys(Keys.CONTROL, 'a')
     git.send_keys("www.github.com/Eray-Koc")
     country = self.driver.find_element(By.NAME, "country")
     country.send_keys(Keys.CONTROL, 'a')
     country.send_keys("Türkiye")
     dropdown = self.driver.find_element(By.NAME, "city")
     dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
     dropdown = self.driver.find_element(By.NAME, "district")
     dropdown.find_element(By.XPATH, "//option[. = 'Avcılar']").click()
     street = self.driver.find_element(By.NAME, "address")
     street.send_keys(Keys.CONTROL, 'a')
     street.send_keys("Yenimahalle mh.")
     about = self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(16) > .form-control")
     about.send_keys(Keys.CONTROL, 'a')
     about.send_keys("Tobeto Yazılım Test Mühendisi")
     sleep(5)
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
     assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Bilgileriniz başarıyla güncellendi."

  @succesful_login_decorator
  def test_profilresmieklekontrol(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "name")))
     self.driver.find_element(By.CSS_SELECTOR, ".photo-edit-btn").click()
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/input[1]").send_keys(r"C:\\Users\\kocer\\OneDrive\\Desktop\\vscodepng.png")
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div[2]/div/div[4]/div[1]/div[2]/button").click()
     try:
         self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/div[1]/div[2]")
         assert True
     except:
         assert False

  @succesful_login_decorator
  def test_TCKN11HanedenFazlaKontrol(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "name")))
     self.driver.find_element(By.NAME, "identifier").send_keys("491382227867")
     value = self.driver.find_element(By.NAME, "identifier").get_attribute("value")
     assert value == "49138222786"
  
  @succesful_login_decorator
  def test_TCKNBosBirakmaKontrol(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "name")))
     tckn = self.driver.find_element(By.NAME, "identifier")
     tckn.send_keys(Keys.CONTROL, 'a')
     tckn.send_keys(Keys.BACK_SPACE)
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button").click()
     assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/span").text == "Satın alınan eğitimlerin faturası için doldurulması zorunlu alan."
  
  @succesful_login_decorator
  def test_MahalleKarakterKontrol(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "name")))
     sleep(4)
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[15]/textarea").send_keys("askdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnasasasass")
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[15]/span[1]")))
     assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[15]/span[1]").text == "En fazla 200 karakter girebilirsiniz"

  @succesful_login_decorator
  def test_HakkindaKarakterKontrol(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "name")))
     sleep(4)
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[16]/textarea").send_keys("askdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnaskdjasndkjnaskjdnakjsdnasasasassaaskdjasndkjnaskjdnakjsdaskdjasndkjnaskjdnakjsdaskdjasndkjnaskjdnakjsdaskdjasndkjnaskjdnakjsdaskdjax")
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/form/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[16]/span[1]")))
     assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[16]/span[1]").text == "En fazla 300 karakter girebilirsiniz"
class TestSENARYOSU14():
  def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("koc1eray@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
          WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          loginbutton.click()
          func(self)
      return login
  
  @succesful_login_decorator
  def test_BasariliDeneyimEklemesi(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")))
     self.driver.find_element(By.NAME, "corporationName").send_keys("TOBETO")
     self.driver.find_element(By.NAME, "position").send_keys("YAZILIM TEST")
     self.driver.find_element(By.CSS_SELECTOR, ".select__input-container").click()
     self.driver.find_element(By.ID, "react-select-5-option-0").click()
     dropdown = self.driver.find_element(By.NAME, "country")
     dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
     self.driver.find_element(By.NAME, "sector").send_keys("YAZILIM")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input").send_keys("03.01.2020")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[7]/div/div/input").send_keys("11.02.2024")
     desc = self.driver.find_element(By.CSS_SELECTOR, ".col-md-12 > .form-control")
     desc.click()
     desc.send_keys("TOBETO")
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
     sleep(3)
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
     assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Deneyim eklendi."

  @succesful_login_decorator
  def test_IsAciklamasiKarakterKontrolu(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")))
     self.driver.find_element(By.NAME, "corporationName").send_keys("TOBETO")
     self.driver.find_element(By.NAME, "position").send_keys("YAZILIM TEST")
     self.driver.find_element(By.CSS_SELECTOR, ".select__input-container").click()
     self.driver.find_element(By.ID, "react-select-5-option-0").click()
     dropdown = self.driver.find_element(By.NAME, "country")
     dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
     self.driver.find_element(By.NAME, "sector").send_keys("YAZILIM")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input").send_keys("03.01.2020")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[7]/div/div/input").send_keys("11.02.2024")
     desc = self.driver.find_element(By.CSS_SELECTOR, ".col-md-12 > .form-control")
     desc.click()
     desc.send_keys("buraonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfburaonharfq")
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
     sleep(3)
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[8]/span")))
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[8]/span").text == "En fazla 300 karakter girebilirsiniz"

  @succesful_login_decorator
  def test_KurumSektorEnAzKarakterKontrolu(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")))
     self.driver.find_element(By.NAME, "corporationName").send_keys("YAZI")
     self.driver.find_element(By.NAME, "position").send_keys("YAZILIM TEST")
     self.driver.find_element(By.CSS_SELECTOR, ".select__input-container").click()
     self.driver.find_element(By.ID, "react-select-5-option-0").click()
     dropdown = self.driver.find_element(By.NAME, "country")
     dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
     self.driver.find_element(By.NAME, "sector").send_keys("YAZI")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input").send_keys("03.01.2020")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[7]/div/div/input").send_keys("11.02.2024")
     desc = self.driver.find_element(By.CSS_SELECTOR, ".col-md-12 > .form-control")
     desc.click()
     desc.send_keys("TOBETO")
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
     sleep(3)
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[1]/span")))
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[1]/span").text == "En az 5 karakter girmelisiniz"
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[4]/span").text == "En az 5 karakter girmelisiniz"

  @succesful_login_decorator
  def test_KurumSektorPozisyonEnFazlaKarakterKontrolu(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")))
     self.driver.find_element(By.NAME, "corporationName").send_keys("TOBEjcsnscajsjcnajcsnasjcnajsnasjnckasjcnajkcnajkcnj")
     self.driver.find_element(By.NAME, "position").send_keys("TOBEjcsnscajsjcnajcsnasjcnajsnasjnckasjcnajkcnajkcnj")
     self.driver.find_element(By.CSS_SELECTOR, ".select__input-container").click()
     self.driver.find_element(By.ID, "react-select-5-option-0").click()
     dropdown = self.driver.find_element(By.NAME, "country")
     dropdown.find_element(By.XPATH, "//option[. = 'İstanbul']").click()
     self.driver.find_element(By.NAME, "sector").send_keys("TOBEjcsnscajsjcnajcsnasjcnajsnasjnckasjcnajkcnajkcnj")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input").send_keys("03.01.2020")
     self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[7]/div/div/input").send_keys("11.02.2024")
     desc = self.driver.find_element(By.CSS_SELECTOR, ".col-md-12 > .form-control")
     desc.click()
     desc.send_keys("TOBETO")
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
     sleep(3)
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[1]/span")))
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[1]/span").text == "En fazla 50 karakter girebilirsiniz"
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[2]/span").text == "En fazla 50 karakter girebilirsiniz"
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[4]/span").text == "En fazla 50 karakter girebilirsiniz"

  @succesful_login_decorator
  def test_KurumSektorPozisyonBosBirakilmaKontrolu(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[1]/span")))
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[1]/span").text == "Doldurulması zorunlu alan*"
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[2]/span").text == "Doldurulması zorunlu alan*"
     assert self.driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/section/div/div/div[2]/form/div/div[4]/span").text == "Doldurulması zorunlu alan*"

class TestSENARYOSU15():
  def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("koc1eray@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
          WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          loginbutton.click()
          func(self)
      return login
  
  @succesful_login_decorator
  def test_BasariliEgitimEkleme(self):
    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
    self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[3]/span[2]")))
    self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[3]/span[2]").click()
    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".select__input-container")))
    sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".select__input-container").click()
    self.driver.find_element(By.ID, "react-select-5-option-2").click()
    self.driver.find_element(By.NAME, "University").send_keys("Erzincan Üniversitesi")
    self.driver.find_element(By.NAME, "Department").send_keys("Yazılım")
    self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(4) .form-control").send_keys("2020")
    self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(5) .form-control").send_keys("2024")
    self.driver.find_element(By.NAME, "Department").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
    assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Eğitim bilgisi eklendi."
class TestSENARYOSU16():
  def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("koc1eray@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
          WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          loginbutton.click()
          func(self)
      return login
  
  @succesful_login_decorator
  def test_BasariliYetkinlikEklenmesi(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[4]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[4]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".css-19bb58m")))
     self.driver.find_element(By.CSS_SELECTOR, ".css-19bb58m").click()
     self.driver.find_element(By.ID, "react-select-5-option-1").click()
     sleep(2)
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
     assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Yetenek eklendi."


  @succesful_login_decorator
  def test_BosBirakilanYetkinlikKontrol(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[4]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[4]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
     sleep(5)
     self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
     assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Herhangi bir yetenek seçmediniz!"

  @succesful_login_decorator
  def test_SecillenYetkinliginSilinmesiKontrol(self):
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[1]/section[3]/div/div/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[4]/span[2]")))
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[4]/span[2]").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div[2]/div[1]/div/button")))
     sleep(4)
     self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div[2]/div[1]/div/button").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-yes")))
     self.driver.find_element(By.CSS_SELECTOR, ".btn-yes").click()
     WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
     assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Yetenek kaldırıldı."



class TestSENARYOSU17():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()
  
   def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("koc1eray@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          self.driver.execute_script("window.scrollTo(0, 500)")
          WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
          loginbutton.click()
          func(self)
      return login
   
   @succesful_login_decorator
   def test_BasariliSertifikaEklemeKontrol(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[5]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[5]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys("TOBETO")
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("2020")
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div[2]/form/div[1]/div[3]/div/div/div/div[2]/div/div[2]/input[1]").send_keys("C:\\Users\\kocer\\OneDrive\\Desktop\\sgk-tescil-ve-hizmet-dokumu.pdf")
      sleep(1)
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[2]")))
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[2]").text == "Sertifikanız eklendi."


   @succesful_login_decorator
   def test_BasarisizSertifikaEklemeKontrol(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[5]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[5]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys("TOBETO")
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("2020")
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div[2]/form/div[1]/div[3]/div/div/div/div[2]/div/div[2]/input[1]").send_keys("C:\\Users\\kocer\\OneDrive\\Desktop\\Clinic.zip")
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/span[1]/div[1]/p[1]")))
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/span[1]/div[1]/p[1]").text == "Sadece image/jpeg, image/png, application/pdf yükleyebilirsiniz"


   @succesful_login_decorator
   def test_SertifikaSilmeKontrol(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[5]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[5]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/span[2]")))
      self.driver.execute_script("window.scrollTo(0, 700)")
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/span[2]").click()
      Button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div/div/div/div[2]/button[2]")))
      sleep(5)
      Button.click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Dosya kaldırma işlemi başarılı."


class TestSENARYOSU18():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()
  
   def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("koc1eray@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          self.driver.execute_script("window.scrollTo(0, 500)")
          WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
          loginbutton.click()
          func(self)
      return login
   
   @succesful_login_decorator
   def test_BasariliSosyalMedyaEklemeKontrol(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[8]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[8]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div[2]/input")))
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div[2]/input").send_keys("Ins", Keys.TAB)
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/input[1]").send_keys("https://www.instagram.com/erykc34/")
      sleep(4)
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Sosyal medya adresiniz başarıyla eklendi."


   @succesful_login_decorator
   def test_SosyalMedyaBosBirakmaKontrol(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[8]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[8]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]").click()
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/span[1]").text == "Doldurulması zorunlu alan*"
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/span[1]").text == "Doldurulması zorunlu alan*"

   @succesful_login_decorator
   def test_SosyalMedyaEklemedeSinirKontrol(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[8]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[8]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div[2]/input")))
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div[2]/input").send_keys("Ins", Keys.TAB)
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/input[1]").send_keys("https://www.instagram.com/erykc34/")
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]").click()
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div[2]/input").send_keys("Tw", Keys.TAB)
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/input[1]").send_keys("https://www.instagram.com/erykc34")
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]").click()
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div[2]/input").send_keys("Li", Keys.TAB)
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/input[1]").send_keys("https://www.instagram.com/erykc3")
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/span[1]")))
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/span[1]").text == "En fazla 3 adet medya seçimi yapılabilir."

   @succesful_login_decorator
   def test_SosyalMedyaSilmeKontrol(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[8]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[8]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/btn[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/btn[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@class='btn btn-yes my-3']")))
      sleep(4)
      self.driver.find_element(By.XPATH, "//*[@class='btn btn-yes my-3']").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Sosyal medya adresiniz başarıyla kaldırıldı."

class TestSENARYOSU19():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()
  
   def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("koc1eray@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          self.driver.execute_script("window.scrollTo(0, 500)")
          WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
          loginbutton.click()
          func(self)
      return login
   
   @succesful_login_decorator
   def test_BasariliYabanciDilEklemeKontrol(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[9]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[9]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div/div/div[1]/div[2]/input")))
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/div/div/div[1]/div[2]/input").send_keys("Alm", Keys.TAB)
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[2]/div/div/div[1]/div[2]/input").send_keys("Tem", Keys.TAB)
      sleep(4)
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Yabancı dil bilgisi eklendi."

   @succesful_login_decorator
   def test_YabanciDilBosBirakmaKontrol(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[9]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[9]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/button[1]")))
      sleep(4)
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/button[1]").click()
      assert self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/p").text == "Doldurulması zorunlu alan*"
      assert self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[2]/p").text == "Doldurulması zorunlu alan*"
      
   @succesful_login_decorator
   def test_YabanciDilSilmeKontrol(self):
      sleep(4)
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[9]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[9]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")))
      element = self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
      action = ActionChains(self.driver)
      action.move_to_element(element).perform()
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[2]").click()
      Yes = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-yes my-3']")))
      Yes.click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Yabancı dil kaldırıldı."

class TestSENARYOSU20():
   def setup_method(self, method):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension("buster.crx")
    self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.get("https://tobeto.com/giris")
    self.driver.maximize_window()
  
   def teardown_method(self, method):
    self.driver.quit()
  
   def succesful_login_decorator(func):
      def login(self):
          WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          username = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[1]/input")
          username.send_keys("koc1eray@gmail.com")
          password = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/div[2]/input")
          password.send_keys("Passw0rd!")
          self.driver.execute_script("window.scrollTo(0, 500)")
          WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")))
          loginbutton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/div[2]/div/div/div[4]/form/button[1]")
          loginbutton.click()
          func(self)
      return login
   
   @succesful_login_decorator
   def test_SifreDegisimindeBosAlanKontrol(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[10]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[10]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/span[1]").text == "Doldurulması zorunlu alan*"
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/span[1]").text == "Doldurulması zorunlu alan*"
      assert self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[3]/span[1]").text == "Doldurulması zorunlu alan*"
   
   @succesful_login_decorator
   def test_SifreKarakterKontrolu(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[10]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[10]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/input")))
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/input").send_keys("Passw0rd!")
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[2]/input").send_keys("123")
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[3]/input").send_keys("123")
      sleep(4)
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Şifreniz en az 6 karakterden oluşmalıdır."

   @succesful_login_decorator
   def test_SifreEslesmeKontrolu(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[10]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[10]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/input")))
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/input").send_keys("Passw0rd!")
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[2]/input").send_keys("Passw0rd!?")
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[3]/input").send_keys("Passw0rd!!")
      sleep(4)
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Girilen şifreler eşleşmiyor kontrol ediniz.."

   @succesful_login_decorator
   def test_SifreTekrariKontrolu(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[10]/span[2]")))
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[1]/a[10]/span[2]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/input")))
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[1]/input").send_keys("Passw0rd!")
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[2]/input").send_keys("Passw0rd!")
      self.driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div[2]/form/div/div[3]/input").send_keys("Passw0rd!")
      sleep(4)
      self.driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/main[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
      assert self.driver.find_element(By.CSS_SELECTOR, ".toast-body").text == "• Yeni şifreniz mevcut şifrenizden farklı olmalıdır."

   
   #BASARILI HESAP SILME


      

