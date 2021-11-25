## 2 Feladat: Matek app

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a Matek app-ot az [https://agreeable-beach-0514a6003.azurestaticapps.net/k2](https://agreeable-beach-0514a6003.azurestaticapps.net/k2) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Matek app tesztelését. Az applikáció minden frissítésnél véletlenszerűen változik!

Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

Az alábbi teszteseteket kell lefedned:

A feladatod, hogy a random számokkal működő matematikai applikációt ellenőrizd. A teszted ki kell, hogy olvassa a három operandust (számot) és a két operátort (műveleti jelet). Ennek megfelelően kell elvégezned a kalkulációt Pythonban. 

* Teszteld le, hogy helyesen jelenik-e meg az applikáció:
    * Egy matematikai képletet látsz aminek a jobb oldalán egy kérdőjellel jelöltül a keresett eredményt, pl 3866-5434*160 = ?
    * A kalkuláció gomb megtalálható és megnyomható.
    * A megoldás üres kezdetben: Eredmény: <üres érték>

* Ellenőrizd, hogy jól működik-e a kalkulátor?

* Ellenőrizd, hogy akárhányszor megnyomható-e a kalkuláció gomb análékül, hogy ez elrontana bármit is.


### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `k2.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(