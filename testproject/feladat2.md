## 2 Feladat: Színes reakció

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ. 

A program töltse be a Színes reakció app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Színes reakció app tesztelését.

Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

Az alábbi teszteseteket kell lefedned:

* Helyesen jelenik meg az applikáció betöltéskor:
    * Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak a `[  ]` szimbólum látszik.
    <szín neve> [     ] == [     ]

* El lehet indítani a játékot a `start` gommbal.
    * Ha elindult a játék akkor a `stop` gombbal le lehet állítani.

* Eltaláltam, vagy nem találtam el.
    * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le 
    amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
      ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen.

### A megoldás beadása
* a megoldásokat a `testproject` mappába tedd, `k2.py`
* a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
* majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
* ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
* a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(