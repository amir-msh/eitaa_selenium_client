# selenium 4
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import selectors as sl
import re
import typing as tp

class EitaaClient():
  _login_url = "https://web.eitaa.com/#/login"

  def __init__(self, phone_number:str):
    self._phone_number=phone_number

  def document_initialised(driver):
      return driver.execute_script("return initialised")

  def load(self):
    # Initializes the webdriver and the ChromeService.
    # Attention: it must be called before using any other function!
    self.service = ChromeService(executable_path=ChromeDriverManager().install())
    self.wd = webdriver.Chrome(service=self.service)
    self.wd.implicitly_wait(5)

  def otp_request(self):
    # Requesting OTP from eitaa.
    self.wd.get(self._login_url)
    phone_el = self.driver.find_element(by=By.NAME, value='phone_number')
    phone_el.send_keys(self.phone_number)
    phone_el.send_keys(Keys.RETURN)
    ok_btn_el = self.wd.find_element(by=By.CSS_SELECTOR, value='div.md_simple_modal_footer > button.btn.btn-md.btn-md-primary')
    ok_btn_el.click()

  def otp_confirm(self, otp:str):
    # confirming OTP
    otp_el = self.wd.find_element(by=By.NAME, value='phone_code')
    otp_el.send_keys(otp)
    WebDriverWait.until(self.wd, timeout=10).until(self.document_initialised)

  def get_chats_list(self) -> tp.List[str] :
    chat_items = self.wd.find_elements(by=By.CSS_SELECTOR, value=sl.chats_name_spans)
    return list(map(self._get_element_text, chat_items))

  def _get_element_text(i) -> str:
    i = i.get_attribute('innerHTML').strip()
    iTagReg = '<i.*></i>$'
    res = re.search(iTagReg, '', i)
    if res:
      i = re.sub(iTagReg, '', i).strip()
      i = re.sub(r'(?<=^\").+?(?=\"$)', '', i)
    return i

