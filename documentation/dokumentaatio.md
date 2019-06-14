# HotellihuoneidenVarausjarjestelma - dokumentaatio

## Linkki Herokussa olevaan sovellukseen
[Herokussa oleva sovellus](https://tsoha-varaussovellus.herokuapp.com/)

## Aihe
- Hotellien varausjärjestelmä

## Kuva tietokantakaaviosta
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/tietokantakaaviot/toteutunut.png "Nykyinen tietokantakaavio")


## TavoiteToiminnot

- kirjautuminen
- Lisaa huone
- listaa huoneet
- listaa asiakkaat
- listaa varaukset
- tee varaus
- peru varaus
- lisävarusteen osto

## Sovelluksessa olevat toiminnot
- kirjautuminen
- rekisteröityminen
- lisää asiakas
- muuta asiakkaan tietoja
- poista asiakas
- listaa huoneet
- lisää huone
- listaa huoneet
- autorisointi (Huoneen lisääminen vaatii ADMIN-oikeudet, muut toiminnot vaativat joko KAYTTAJA-oikeudet tai ei mitään oikeuksia)
- etusivulla monimutkainen kysely, joka tulostaa käyttäjät, joilla ei ole asiakkaita
- Lisää varaus
- Listaa varaukset



### Tietokannan kaynnistaminen pythonilla

```
python run.py
```

## Esimerkkeja kayttotarkoituksista

#### Aloitussivu
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Aloitussivu_uusin.png "Kuva aloitussivusta")
- Kuvasta näkyy myös käyttäjät, joilla ei ole yhtään asiakkaita. Kysely täyttää kurssin vaatimukset monimutkaisesta kyselystä.

#### Kirjautuminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Kirjautuminen_sivu.png "Kuva kirjautumissivusta")

#### Rekisteröityminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/rekisteroityminen.png "Kuva rekisteröitymissivusta")
- Linkki rekisteröitymiseen on aloitussivun oikeassa ylänurkassa.
- Syötä nimi, käyttäjänimi ja salasana (kaikkien minimi 2 merkkiä ja max 144 merkkiä).
- Huom! Rekisteröityessäsi sinulla on vain käyttäjä-oikeudet eikä admin-oikeuksia.

#### Asiakkaiden listaaminen, tietojen muuttaminen ja asiakkaan poistaminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Listaa_asiakkaat.png "Asiakkaiden listaaminen, tietojen muuttaminen ja poistaminen")
- CRUD
- Asiakkaan poistaminen vaatii kirjautumisen. User voi tehdä.

#### Asiakkaiden lisaaminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Lis%C3%A4%C3%A4_asiakas.png "Lomake, jolla asiakas lisätään.")
- Vaatii kirjautumisen. User voi tehdä.


#### Hotellihuoneen lisääminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Lis%C3%A4%C3%A4_huone.png "Lomake, jolla huone lisätään.")

- vaatii admin-oikeuksilla kirjautumisen, pitää syöttää huonenumero (kokonaisluku), hinta (kokonaisluku) ja huoneen tyyppi (Esimerkiksi economy tai deluxe)
- painikkeen painaminen lisää huoneen

#### Hotellihuoneiden listaus
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Listaa_huoneet.png "Huoneiden listaus, huonenumero, hinta, tyyppi")

- onnistuu huoneiden listaaminen sivulla, ei vaadi kirjautumista

#### Varauksen lisääminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Varauksen_tekeminen.png "Lomake, jolla varaus lisätään.")

- Vaatii kirjautumisen. Pitää syöttää huone_id, asiakas_id, huoneen hinta ja varausviikko.
- painikkeen painaminen lisää varauksen.

#### Varausten listaus
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Listaa_varaukset.png "Varausten listaaminen")

- Onnistuu "Listaa varaukset"-linkkiä painamalla.



#### Schema 
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Uusin_Schema.png "Kuva tietokannan nykyisestä skeemasta")







