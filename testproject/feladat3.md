## 3 Feladat: Nagybetűs városnév mező

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a Nagybetűs város appot az [https://agreeable-beach-0514a6003.azurestaticapps.net/k3](https://agreeable-beach-0514a6003.azurestaticapps.net/k3) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Nagybetűs város app tesztelését.

Az applikáció minden frissítésnél véletlenszerűen változik!

Feladatod, hogy megtaláld azt a városnevet, ami **csupa nagyvetűvel** van írva és kitöltsd a form-ban a mezőt és ellnörizd le, hogy eltaláltad-e.

Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

Az alábbi teszteseteket mindenkép fedd le:
* Helyesen jelenik meg az applikáció:
    * a városnév input mező üres
    * az Ellenőrzés gomb látható és engedélyezve van
    * Az 'Eredmény:' feladat nem látható
* Ellenőrizd a helye működést:
    * Keressd meg és írd be a random nagybetűs városnevet
    * Ellenőrizd, hogy elfogadja-e az applikáció helyes megfejtésnek
* Ellenőrizd a hibás esetet:
    * Ha rossz városnevet adunk meg akkor nem szabad, hogy elfogadja a megfejtést az applikáció

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `k3.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(