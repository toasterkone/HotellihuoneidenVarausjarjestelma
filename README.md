# HotellihuoneidenVarausjarjestelma

Toteutus hotellihuoneiden varausjärjestelmälle.

Aihe: Hotellien varausjärjestelmä

Aihekuvaus:
Hotellien varausjärjestelmä sisältää huoneita halutun määrän ja huoneita voidaan lisätä halutessa. Huoneita voidaan varata ja huoneille voidaan ostaa lisavarusteita. Huoneita on eri hintaisia ja tyyppisiä. Varauksia voidaan perua. Varausjärjestelmä sisältää alustavasti kolme tietokantataulua: asiakas, hotellihuone, lisavaruste.

Asiakkaasta tallennetaan ainakin nimi, puhelinnumero, sähköposti. Hotellihuoneella on huonenumero, hinta, tyyppi ja hotellihuoneelle voidaan kirjata asiakas. Lisävarusteella on hinta, nimi ja tieto mihin huoneeseen se on varattu.

Huoneen varausta varten pitää asiakkaan maksaa varausmaksu, joka riippuu huoneesta. 


Tietokantataulut: Asiakas, Hotellihuone, Lisavaruste

Asiakas((PK) id:Integer, nimi:varchar, puhnum:varchar,email:varchar)
Hotellihuone((PK)id:int, tyyppi:Varchar, hinta:int, vapaa:boolean, (FK)asiakas_id:Asiakas)
Lisavaruste((PK)id:int, hinta:int, nimi:varchar, (FK)hotellihuone_id:Hotellihuone)

Toiminnot:
- Kirjautuminen
- Lisaa huone
- listaa huoneet
- listaa asiakkaat
- tee varaus
- peru varaus
- lisävarusteen osto
