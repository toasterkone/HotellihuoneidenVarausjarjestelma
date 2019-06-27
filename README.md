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


## Dokumentaatio

- [Dokumentaatiota sisaltava kansio](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/tree/master/documentation )
- [Käyttöohjeet](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kaytto_ohje.md )
- [Asennusohjeet](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/asennusohje.md )
- [Create Table -lauseet](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/SQL_Create_Table_lauseet.md )
- [Käyttäjätarinat](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/user_stories.md )
- [Omat kokemukset](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/omat_kokemukset.md )
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



## Toteutuneet ominaisuudet

- Lisää asiakas
- Lisää huone
- Lisää varaus
- Listaa asiakkaat
- Listaa huoneet
- Listaa varaukset
- Peru varaus 
- CRUD-toiminnallisuudet asiakkaalle (lisäys, muokkaus, listaus ja poistaminen)
- Kirjautuminen 
- Rekisteröityminen (luo uudet USER-käyttäjän)
- Kurssin monimutkaisuuden vaatimuksen täyttävä yhteenvetokysely etusivulla, joka kertoo käyttäjät, jotka eivät ole lisänneet asiakkaita. Tämä näkyy aloitussivulla vain, jos on kirjautunut ADMIN-oikeuksilla.
- Autorisointi (huoneen lisääminen vaatii ADMIN-oikeudet, muut toiminnot vaativat joko USER-oikeudet tai ei mitään oikeuksia). 
- Osa tiedoista validoidaan. Esimerkiksi asiakkaan tietojen pitää täyttää tietyt vaatimukset.
- Monen suhde moneen taulut (lisavaruste ja huone) ja liitostaulu (huonelisavaruste)

## Toteutumattomat ominaisuudet ja jatkokehitys

- Lisävarusteisiin liittyvät toiminnallisuudet, kuten lisävarusteiden lisääminen ja listaaminen, lisävarusteiden lisäys huoneelle ja huoneiden lisävarusteiden listaus.
- Asiakkaan varausten hakeminen nimellä.
- Yhdellä varauksella voisi varata useita huoneita.
- Varausten hakeminen tietylle aikavälille.
- Listausten (asiakkaat, huoneet, varaukset, lisävarusteet) sivutus.
- Varausajan muuttaminen realistisemmaksi. Tällä hetkellä huone varataan aina viikoksi kerrallaan, todellisempaa olisi, jos huone varattaisiin haluttujen päivien ajaksi.
- Admin-käyttäjälle lisää tominnallisuuksia, kuten muuta toisten käyttäjien oikeuksia ja poista käyttäjiä.
- Sivuston tyylittelyn/käytettävyyden parantaminen.
- Sovelluksen muuttaminen siten, että sitä voi käyttää asiakkaat ja työntekijät/hotellinomistaja. Asiakkaan rekisteröityminen lisäisi asiakkaan automaattisesti asiakas-tauluun. Asiakkaalla vain oikeudet listata huoneet, tehdä varaus ja listata omat varauksensa.
- Hinta-attribuuttien muuttaminen kokonaisluvuista realistisemmiksi esimerkiksi Numeric-tyyppisiksi.

## Normalisointi

Tietokantaa ei ole normalisoitu 3:een normaalimuotoon, sillä esimerkiksi varaus-taulussa on ns. ylimääräistä tietoa (hinta). Tämä sen takia, että tietyissä tauluissa käytettävyys helpottuu, kun sisällytetään ylimääräistä tietoa.

## Sovelluksen tietokantataulut
- Asiakas
- Huone
- account(käyttäjä-taulu)
- Rooli
- Huone
- Lisavaruste
- huonelisavaruste (liitostaulu)







