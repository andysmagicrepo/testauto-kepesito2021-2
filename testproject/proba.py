# feladat leírás helye (feladat.md)

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
URL = "https://agreeable-beach-0514a6003.azurestaticapps.net/k2"


elso_szam = driver.find_elemet_by_id("num1").text
elso_operator_char = driver.find_elemet_by_id("op1")
masodik_szam = driver.find_element_by_id("num2")
masodik_operator_char = driver.find_elemet_by_id("op2")
harmadik_szam = driver.find_element_by_id("num3")
kerdojel = driver.find_elemet_by_id()
alk_eredmeny = driver.find_elemet_by_id("result")
kalkulacio_gomb = driver.find_elemet_by_id("submit")

op1 = driver.find_element_by_id("op1")
op2 = driver.find_element_by_id("op2")
num1 = driver.find_element_by_id("num1")
num2 = driver.find_element_by_id("num2")
num3 = driver.find_element_by_id("num3")
submit_button = driver.find_element_by_id("submit")

def assemble_expression(*args):
    return "{}{}{}{}{}".format(*args)


def test_evaluate_expression():
    submit_button.click()
    result_text = driver.find_element_by_id("result")
    ex = assemble_expression(elso_szam.text, elso_operator_char.text, masodik_szam.text, masodik_operator_char.text, harmadik_szam.text)
    assert eval(ex) == int(alk_eredmeny)

test_evaluate_expression()
