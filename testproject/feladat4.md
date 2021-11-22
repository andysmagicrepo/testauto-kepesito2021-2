## 4 Feladat: Password validation

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a Password validation app-ot az [https://agreeable-beach-0514a6003.azurestaticapps.net/k4](https://agreeable-beach-0514a6003.azurestaticapps.net/k4) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Password validation app tesztelését.

Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

Az alábbi teszt eseteket kell kidolgozzad:

* Helyesen jelenik meg az applikáció:
    * Megjelennek a username illetve password mezők, de üres a tartalmuk
    * Van submit gomb
    * Nincs hiba a képernyőn

* Helyes kitöltés - nincs hiba:
    * username: kisstamas
    * password: Abcd123!
    * Minden kategóriában pozitív a jelszó ellenőrzés kimenete
    
* Helytelen kitöltés - 4 hiba
    * username: kisstamas
    * password: !
    * Minden kategóriában negatív a jelszó ellenőrzés kimenete


### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `k4.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(