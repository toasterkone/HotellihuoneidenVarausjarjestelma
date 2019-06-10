# HotellihuoneidenVarausjarjestelma - dokumentaatio

## Linkki Herokussa olevaan sovellukseen
["Herokussa oleva sovellus"](https://tsoha-varaussovellus.herokuapp.com/)

## Aihe
- Hotellien varausjärjestelmä

## Kuva tietokantakaaviosta
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/tietokantakaaviot/toteutunut_1.png "Nykyinen tietokantakaavio")


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
- lisää asiakas
- muuta asiakkaan tietoja
- poista asiakas
- listaa huoneet
- lisää huone
- listaa huoneet



### Tietokannan kaynnistaminen pythonilla

```
python run.py
```

## Esimerkkeja kayttotarkoituksista

#### Aloitussivu
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/aloitussivu.png "Kuva aloitussivusta")
- Kuvasta näkyy myös käyttäjät, joilla ei ole yhtään asiakkaita.

#### Kirjautuminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/kirjautuminen.png "Kuva kirjautumissivusta")


#### Asiakkaiden listaaminen, tietojen muuttaminen ja asiakkaan poistaminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Asiakkaiden%20listaaminen%20ja%20poistaminen.png "Asiakkaiden listaaminen ja poistaminen")
- Asiakkaan poistaminen vaatii kirjautumisen.

#### Asiakkaiden lisaaminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/asiakkaan%20lisaaminen.png "Lomake, jolla asiakas lisätään.")
- Vaatii kirjautumisen.


#### Hotellihuoneen lisääminen
- vaatii kirjautumisen, pitää syöttää huonenumero (kokonaisluku), hinta (kokonaisluku) ja huoneen tyyppi (Esimerkiksi economy tai deluxe)
- painikkeen painaminen lisää huoneen

#### Hotellihuoneiden listaus
- onnistuu huoneiden listaaminen sivulla

#### Schema ja käyttäjän lisääminen SQLiten avulla
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/schema%20ja%20kayttajan%20lisaaminen.png "SQLiten kaytto")







