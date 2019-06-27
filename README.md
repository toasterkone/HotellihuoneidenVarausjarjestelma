# VarausApp

## Tietokantasovellus-kurssi, alkukesä 2019

## Aihe
- Hotellin varausjärjestelmä

## Aihekuvaus

Sovellus toimii hotellin järjestelmänä, jossa voi hallinnoida asiakkaita, varauksia ja huoneita.

Varausjärjestelmää käyttävät hotellin työntekijät ja hotellinomistaja. Sovellus sisältää toiminnallisuudet lisätä asiakkaita, huoneita ja varauksia. Sovelluksessa on myös mahdollista listata asiakkaat, huoneet ja varaukset. Asiakkaisiin liittyy CRUD-toiminnallisuudet eli asiakkaan voi lisätä, asiakkaan tietoja voi muuttaa, asiakkaat voi listata ja asiakkaan voi poistaa. 

Sovellus tarjoaa uudelle työntekijälle mahdollisuuden rekisteröityä sovelluksen käyttäjäksi eli työntekijä rekisteröityy antamalla koko nimensä (etu- ja sukunimi), sekä käyttäjänimen ja salasanan. Rekisteröityessään työntekijä ei saa ADMIN-oikeuksia, mutta hän pystyy tekemään kaiken muun sovelluksessa paitsi huoneen lisäyksen. Työntekijät pystyvät käyttämään sovellusta ilman kirjautumista, mutta tässä tilanteessa he pystyvät vain käyttämään listaustoimintoja. Hotellinomistajalla on ADMIN-oikeudet eli hän pystyy lisäämään huoneita tietokantaan.
 
## Linkki Herokussa sijaitsevaan sovellukseen
[Herokussa oleva sovellus](https://tsoha-varaussovellus.herokuapp.com/)

## Osa sovelluksen kehityksessä käytetyistä työkaluista 
- SQLite, PostgreSQL, SQLAlchemy, Flask, Python, HTML, Bootstrap

## Dokumentaatio

- [Dokumentaatiota sisaltava kansio](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/tree/master/documentation )
- [Käyttöohjeet](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kaytto_ohje.md )
- [Asennusohjeet](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/asennusohje.md )
- [Create Table -lauseet](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/SQL_Create_Table_lauseet.md )
- [Käyttäjätarinat](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/user_stories.md )
- [Omat kokemukset](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/omat_kokemukset.md )
- [Toteutuneet/toteutumattomat ominaisuudet ja jatkokehitys](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/ominaisuudet_ja_jatkokehitys.md )
- [Tietokantakaavio](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/tietokantakaaviot/toteutunut_tietokantakaavio.png )


## Admin-oikeudet omaava käyttäjä ja kirjautumiseen vaaditut tiedot

- Tällä tilillä pystyy käyttämään kaikkia verkkosovelluksen toimintoja.

| Username | Password |
|:--------:|:--------:|
| hello    |    world |

## User-oikeudet omaava käyttäjä ja kirjautumiseen vaaditut tiedot

- Tällä tilillä pystyy käyttämään kaikkia verkkosovelluksen toimintoja, paitsi huoneen lisäystä.

| Username | Password |
|:--------:|:--------:|
| hei      |   maailma|

## Normalisointi

Tietokantaa ei ole täysin normalisoitu 3:een normaalimuotoon, sillä esimerkiksi varaus-taulussa on ns. ylimääräistä tietoa (hinta). Tämä sen takia, että tietyissä tauluissa käytettävyys helpottuu, kun sisällytetään ylimääräistä tietoa.

## Sovelluksen tietokantataulut
- Asiakas
- Huone
- account(käyttäjä-taulu)
- Rooli
- Huone
- Lisavaruste
- huonelisavaruste (liitostaulu)







