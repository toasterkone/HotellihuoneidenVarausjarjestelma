# HotellihuoneidenVarausjarjestelma - dokumentaatio

## Linkki Herokussa olevaan sovellukseen
["Herokussa oleva sovellus"](https://tsoha-varaussovellus.herokuapp.com/)

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
- autorisointi
- etusivulla monimutkainen kysely, joka tulostaa käyttäjät, joilla ei ole asiakkaita



### Tietokannan kaynnistaminen pythonilla

```
python run.py
```

## Esimerkkeja kayttotarkoituksista

#### Aloitussivu
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Aloitus_sivu.png "Kuva aloitussivusta")
- Kuvasta näkyy myös käyttäjät, joilla ei ole yhtään asiakkaita. Kysely täyttää kurssin vaatimukset monimutkaisesta kyselystä.

#### Kirjautuminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/kirjautuminen.png "Kuva kirjautumissivusta")

#### Rekisteröityminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/kirjautuminen.png "Kuva rekisteröitymissivusta")
- Linkki rekisteröitymiseen on aloitussivun oikeassa ylänurkassa.
- Syötä nimi, käyttäjänimi ja salasana (kaikkien minimi 2 merkkiä ja max 144 merkkiä).
- Huom! Rekisteröityessäsi sinulla on vain käyttäjä-oikeudet eikä admin-oikeuksia.

#### Asiakkaiden listaaminen, tietojen muuttaminen ja asiakkaan poistaminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Asiakkaiden%20listaaminen%20ja%20poistaminen.png "Asiakkaiden listaaminen ja poistaminen")
- Asiakkaan poistaminen vaatii kirjautumisen. User voi tehdä.

#### Asiakkaiden lisaaminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/asiakkaan%20lisaaminen.png "Lomake, jolla asiakas lisätään.")
- Vaatii kirjautumisen. User voi tehdä.


#### Hotellihuoneen lisääminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Huoneen_lisaaminen.png "Lomake, jolla huone lisätään.")

- vaatii admin-oikeuksilla kirjautumisen, pitää syöttää huonenumero (kokonaisluku), hinta (kokonaisluku) ja huoneen tyyppi (Esimerkiksi economy tai deluxe)
- painikkeen painaminen lisää huoneen

#### Hotellihuoneiden listaus
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Huoneiden_listaaminen.png "Huoneiden listaus, huonenumero, hinta, tyyppi")

- onnistuu huoneiden listaaminen sivulla

#### Schema 
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/schema%20ja%20kayttajan%20lisaaminen.png "Kuva tietokannan skeemasta")







