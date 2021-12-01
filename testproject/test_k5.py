# ## 5 Feladat: Large Tic Tac Toe
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a Large Tic Tac Toe app-ot az [https://agreeable-beach-0514a6003.azurestaticapps.net/k5](https://agreeable-beach-0514a6003.azurestaticapps.net/k5) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a Large Tic Tac Toe app tesztelését.
#
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!
#
# A feladatod az alábbi tesztesetek lefejlesztése:
# * Az applikáció helyesen megjelenik:
#     * A Tic Tac Toe tabla 12 x 12 meretu (144 cellat tartalmaz)
#     * Minden cell ?-et tartalmaz
#
# * Alap játékszabályok ellenőrzése:
#     * Az első játékos (első gombnyomás) megnyom egy cellát, ami ezután X karaktert kell, hogy tartalmazzon
#     * A második játékos (második gombnyomás) megnyom egy cellát, ami ezután 0 karaktert kell, hogy tartalmazzon
#
# * Győztes
#     * Ellenőrizzük az "öt ugyanolyan győz" szabályt vizszintesen
#     * Ellenőrizzük az "öt ugyanolyan győz" szabályt függőlegesen
#
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `k5.py`
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
URL = "https://agreeable-beach-0514a6003.azurestaticapps.net/k5"

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