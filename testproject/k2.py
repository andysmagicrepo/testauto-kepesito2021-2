# ## 2 Feladat: Matek app
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
# A program töltse be a Matek app-ot az [https://agreeable-beach-0514a6003.azurestaticapps.net/k2](https://agreeable-beach-0514a6003.azurestaticapps.net/k2) oldalról.
# Feladatod, hogy automatizáld selenium webdriverrel a Matek app tesztelését. Az applikáció minden frissítésnél véletlenszerűen változik!
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!
# Az alábbi teszteseteket kell lefedned:
# A feladatod, hogy a random számokkal működő matematikai applikációt ellenőrizd. A teszted ki kell, hogy olvassa a három operandust (számot) és a két operátort (műveleti jelet). Ennek megfelelően kell elvégezned a kalkulációt Pythonban.
#
# * Teszteld le, hogy helyesen jelenik-e meg az applikáció:
#     * Egy matematikai képletet látsz aminek a jobb oldalán egy kérdőjellel jelöltül a keresett eredményt, pl 3866-5434*160 = ?
#     * A kalkuláció gomb megtalálható és megnyomható.
#     * A megoldás üres kezdetben: Eredmény: <üres érték>
#
# * Ellenőrizd, hogy jól működik-e a kalkulátor?
#
# * Ellenőrizd, hogy akárhányszor megnyomható-e a kalkuláció gomb análékül, hogy ez elrontana bármit is.
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `k2.py`
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

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
#driver.set_window_rect(1200, 400, 1300, 1000)
URL = "https://agreeable-beach-0514a6003.azurestaticapps.net/k2"

driver.get(URL)
time.sleep(2)

# kiemelés elements
elso_szam = int(driver.find_elemet_by_id("num1").text)
masodik_szam = int(driver.find_element_by_id("num2").text)
harmadik_szam = int(driver.find_element_by_id("num3").text)
elso_operator_char = driver.find_elemet_by_id("op1").text
masodik_operator_char = driver.find_elemet_by_id("op2").text

kerdojel = driver.find_elemet_by_id()
alk_eredmeny = driver.find_elemet_by_id("result")
kalkulacio_gomb = driver.find_elemet_by_id("submit")


def calculator():
    eredmeny = eval(f"{elso_szam}{elso_operator_char}{masodik_szam}{masodik_operator_char}{harmadik_szam}")
    assert eredmeny == int(alk_eredmeny.text)

# TC1-helyes kitöltés
#* Egy matematikai képletet látsz aminek a jobb oldalán egy kérdőjellel jelöltül a keresett eredményt, pl 3866-5434*160 = ?
#     * A kalkuláció gomb megtalálható és megnyomható.
#     * A megoldás üres kezdetben: Eredmény: <üres érték>
def tc1():
    # kezdeti ellenorzes
    assert alk_eredmeny == ""
    assert (kalkulacio_gomb.isDisplayed() and kalkulacio_gomb.isEnabled) == true

# TC2-helytelen kitöltés
# Ellenőrizd, hogy jól működik-e a kalkulátor?
def tc2():
    kalkulacio_gomb.click()
    calculator()
    pass

# TC3-helytelen kitöltés
# * Ellenőrizd, hogy akárhányszor megnyomható-e a kalkuláció gomb análékül, hogy ez elrontana bármit is.
def tc3():
    for i in range(100):
        kalkulacio_gomb.click()
        calculator()
        time.sleep(1)

# test_tc1()
# test_tc2()
# test_tc3()
tc1()
tc2()
tc3()
#driver.quit()