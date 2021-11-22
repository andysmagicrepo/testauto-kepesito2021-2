## 1 Feladat: Haromszög kerülete

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a Háromszög kerülete app-ot az [https://agreeable-beach-0514a6003.azurestaticapps.net/k1](https://agreeable-beach-0514a6003.azurestaticapps.net/k1) oldalról. 

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a Háromszög kerülete appban:

Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

* Helyesen jelenik meg az applikáció betöltéskor:
    * a: <üres>
    * b: <üres>
    * c: <üres>
    * kerület: <nem látszik>

* Számítás helyes, megfelelő bemenettel
    * a: 2
    * b: 3
    * c: 10
    * kerület: 15

* Üres kitöltés:
    * a: <üres>
    * b: <üres>
    * c: <üres>
    * kerület: NaN   

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `k1.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(