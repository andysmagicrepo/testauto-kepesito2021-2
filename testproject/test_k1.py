# ## 1 Feladat: Haromszög kerülete
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
# A program töltse be a Háromszög kerülete app-ot az [https://agreeable-beach-0514a6003.azurestaticapps.net/k1](https://agreeable-beach-0514a6003.azurestaticapps.net/k1) oldalról.
# Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a Háromszög kerülete appban:
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!
#
# * Helyesen jelenik meg az applikáció betöltéskor:
#     * a: <üres>
#     * b: <üres>
#     * c: <üres>
#     * kerület: <nem látszik>
#
# * Számítás helyes, megfelelő bemenettel
#     * a: 2
#     * b: 3
#     * c: 10
#     * kerület: 15
#
# * Üres kitöltés:
#     * a: <üres>
#     * b: <üres>
#     * c: <üres>
#     * kerület: NaN
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `k1.py`
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
URL = "https://agreeable-beach-0514a6003.azurestaticapps.net/k1"

driver.get(URL)
time.sleep(2)

# kiemelés elements
a_mezo = driver.find_element_by_id("a")
b_mezo = driver.find_element_by_id("b")
c_mezo = driver.find_element_by_id("c")
kalkulacio_gomb = driver.find_element_by_id("submit")
eredmeny = driver.find_element_by_id("result")

# kiemelés tesztadat
a_ertekek = ["", "2", ""]
b_ertekek = ["", "3", ""]
c_ertekek = ["", "10", ""]
elvart_eredmenyek = ["", "15", "NaN"]


def kuld_es_szamol(a, b, c, kerulet):
    a_mezo.clear()
    b_mezo.clear()
    c_mezo.clear()
    a_mezo.send_keys(a)
    b_mezo.send_keys(b)
    c_mezo.send_keys(c)
    kalkulacio_gomb.click()
    #eredmeny = driver.find_element_by_id("result")
    assert eredmeny.text == kerulet
    print(eredmeny)

# TC1-helyes kitöltés
# Helyesen jelenik meg az applikáció betöltéskor:
#     * a: <üres>
#     * b: <üres>
#     * c: <üres>
#     * kerület: <nem látszik>
def test_tc1():
    # assert a_mezo == ""
    # assert b_mezo == ""
    # assert c_mezo == ""
    #assert not eredmeny.is_displayed()
    kuld_es_szamol(a_ertekek[0], b_ertekek[0], c_ertekek[0], elvart_eredmenyek[0])
    time.sleep(1)

# TC2-helytelen kitöltés
# * Számítás helyes, megfelelő bemenettel
#     * a: 2
#     * b: 3
#     * c: 10
#     * kerület: 15
def test_tc2():
    kuld_es_szamol(a_ertekek[1], b_ertekek[1], c_ertekek[1], elvart_eredmenyek[1])

# TC3-helytelen kitöltés
# * Üres kitöltés:
#     * a: <üres>
#     * b: <üres>
#     * c: <üres>
#     * kerület: NaN
def test_tc3():
    kuld_es_szamol(a_ertekek[2], b_ertekek[2], c_ertekek[2], elvart_eredmenyek[2])

test_tc1()
test_tc2()
test_tc3()

#driver.quit()