# HotellihuoneidenVarausjarjestelma

Toteutus hotellihuoneiden varausjärjestelmälle. Varausjärjestelmä sisältää toiminnot mm. varausten tekemiseen, huoneiden lisäämiseen ja asiakkaiden listaamiseen.

Aihe: Hotellien varausjärjestelmä

Tietokantataulut: Asiakas, Hotellihuone, Lisavaruste

Asiakas((PK) id:Integer, nimi:varchar, puhnum:varchar,email:varchar)
Hotellihuone((PK)id:int, tyyppi:Varchar, hinta:int, vapaa:boolean, huonenAsiakas_id:int, asiakas_id:Asiakas)
Lisavaruste((PK)id:int, hinta:int, nimi:varchar, hotellihuone_id:Hotellihuone)

Toiminnot:

- Lisaa huone
- listaa huoneet
- listaa asiakkaat
- tee varaus
- peru varaus
- lisävarusteen osto
