# ## 3 Feladat: Nagybetűs város
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
# A program töltse be a Nagybetűs város appot az [https://agreeable-beach-0514a6003.azurestaticapps.net/k3](https://agreeable-beach-0514a6003.azurestaticapps.net/k3) oldalról.
# Feladatod, hogy automatizáld selenium webdriverrel a Nagybetűs város app tesztelését.
# Az applikáció minden frissítésnél véletlenszerűen változik!
# Feladatod, hogy megtaláld azt a városnevet, ami **csupa nagyvetűvel** van írva és kitöltsd a form-ban a mezőt és ellnörizd le, hogy eltaláltad-e.
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!
#
# Az alábbi teszteseteket mindenkép fedd le:
# * Helyesen jelenik meg az applikáció:
#     * a városnév input mező üres
#     * az Ellenőrzés gomb látható és engedélyezve van
#     * Az 'Eredmény:' feladat nem látható
# * Ellenőrizd a helye működést:
#     * Keressd meg és írd be a random nagybetűs városnevet
#     * Ellenőrizd, hogy elfogadja-e az applikáció helyes megfejtésnek
# * Ellenőrizd a hibás esetet:
#     * Ha rossz városnevet adunk meg akkor nem szabad, hogy elfogadja a megfejtést az applikáció
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `k3.py`
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
URL = "https://agreeable-beach-0514a6003.azurestaticapps.net/k3"

driver.get(URL)
time.sleep(2)

# kiemelés elements

# kiemelés tesztadat
#test_data = []
#test_results = []

def clear_and_fill_input(element, text):
    pass
    # element.clear()
    # element.send_keys(text)

# TC1-helyes kitöltés
#def test_proper_card_deck():
def test_tc1():
    pass

# TC2-helytelen kitöltés
#def test_initial_submit_enabled():
def test_tc2():
    driver.get(URL)     # weblap alaphelyzetet eredményez
    pass

# TC3-helytelen kitöltés
#def test_initial_card_list_empty():
def test_tc3():
    pass

test_tc1()
test_tc2()
test_tc3()

#driver.quit()