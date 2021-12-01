# ## 4 Feladat: Password validation
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
# A program töltse be a Password validation app-ot az [https://agreeable-beach-0514a6003.azurestaticapps.net/k4](https://agreeable-beach-0514a6003.azurestaticapps.net/k4) oldalról.
# Feladatod, hogy automatizáld selenium webdriverrel a Password validation app tesztelését.
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!
#
# Az alábbi teszt eseteket kell kidolgozzad:
#
# * Helyesen jelenik meg az applikáció:
#     * Megjelennek a username illetve password mezők, de üres a tartalmuk
#     * Van submit gomb
#     * Nincs hiba a képernyőn
#
# * Helyes kitöltés - nincs hiba:
#     * username: kisstamas
#     * password: Abcd123!
#     * Minden kategóriában pozitív a jelszó ellenőrzés kimenete
#
# * Helytelen kitöltés - 4 hiba
#     * username: kisstamas
#     * password: !
#     * Minden kategóriában negatív a jelszó ellenőrzés kimenete
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `k4.py`
# * a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
# * majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
# * ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
# * akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
# * a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
# * nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
from pprint import pprint
import csv
#import pytest

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)
URL = "https://agreeable-beach-0514a6003.azurestaticapps.net/k4"

driver.get(URL)
time.sleep(2)


driver.get("https://agreeable-beach-0514a6003.azurestaticapps.net/k4")
    time.sleep(1)


# Kitöltendő mező és klikkelendő gomb
user_name = driver.find_element_by_id("usrname")
password = driver.find_element_by_id("psw")
submit_button = driver.find_element_by_xpath("/html/body/div[1]/form/input[3]")

# üres tartalom ell
assert user_name.isDisplayed
assert password.isDisplayed
assert user_name == ""
assert password == ""

test_data_UN = ["kisstamas", "kisstamas"]
test_data_Pw = ["Abcd123!", "!"]
expected_error_message = [""]


def email_and_click(input_data):
    """beviteli mező törlése és új adatbevitel"""
    user_name.clear()
    user_name.send_keys(input_data)
    submit_button.click()
    time.sleep(1)


# TC1 - Helyes kitöltés
def test_TC01():
    email_and_click(test_data[0])
    error_1 = driver.find_elements_by_class_name("validation-error")
    assert len(error_1) == 0

# TC2 - Helytelen kitöltés
def test_TC02():
    email_and_click(test_data[1])
    error_2 = driver.find_element_by_class_name("validation-error").text
    assert error_2 == expected_error_message[1]

# TC3 - üres kitöltés
def test_TC03():
    email_and_click(test_data[2])
    error_3 = driver.find_element_by_class_name("validation-error").text
    assert error_3 == expected_error_message[2]
    time.sleep(1)

test_TC01():
test_TC02():
test_TC03():
