# VarausApp

# Tietokantasovellus-kurssi

## Linkki Herokussa sijaitsevaan sovellukseen
[Herokussa oleva sovellus](https://tsoha-varaussovellus.herokuapp.com/)


## HotellihuoneidenVarausjarjestelma

## Aihe
- Hotellien varausjärjestelmä

## Aihekuvaus

Hotellien varausjärjestelmä sisältää huoneita halutun määrän ja huoneita voidaan lisätä halutessa. Huoneita voidaan varata ja huoneille voidaan ostaa lisavarusteita. Huoneita on eri hintaisia ja tyyppisiä. Varauksia voidaan perua. Varausjärjestelmä sisältää alustavasti neljä tietokantataulua: asiakas, hotellihuone, lisavaruste ja varaus. Hotellihuoneet varataan aina viikko kerrallaan ja varausajoista pidetään kirjaa viikkonumeroiden avulla.

Asiakkaasta tallennetaan ainakin etu- ja sukunimi, puhelinnumero, sähköposti. Hotellihuoneella on huonenumero, hinta, tyyppi. Lisävarusteella on hinta, nimi ja tieto mihin varaukseen se liittyy.

Huoneen varausta varten pitää asiakkaan maksaa varausmaksu, joka riippuu huoneesta. 


## TavoiteTietokantataulut
- Asiakas
- Hotellihuone 
- Lisavaruste
- Varaus
- account(käyttäjä-taulu)
- Rooli

## Tämänhetkiset Tietokantataulut
- Asiakas
- Huone
- account(käyttäjä-taulu)
- Rooli
- Huone


## Kuva tavoitetietokantakaaviosta
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/tietokantakaaviot/toteutunut_2.png "Tavoitetietokantakaavio")

## Kuva tämänhetkisestä tietokantakaaviosta
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/tietokantakaaviot/toteutunut_5.png "Toteutunut tietokantakaavio")

## TavoiteToiminnot

- kirjautuminen
- Lisaa huone
- listaa huoneet
- listaa asiakkaat
- listaa varaukset
- tee varaus
- peru varaus
- lisävarusteen osto

## Tämänhetkiset toiminnot sovelluksessa
- kirjautuminen
- Asiakas-taulun CRUD-toiminnot (alla listattuna)
- rekisteröityminen (jonka jälkeen kayttaja-oikeudet)
- listaa asiakkaat
- poista asiakas
- muokkaa asiakkaan tiedot
- lisää huone
- listaa huoneet
- monimutkainen kysely etusivulla, joka näyttää käyttäjät, joilla ei ole asiakkaita. Täyttää kurssin vaatimukset.
- autorisointi (Huoneen lisääminen vaatii ADMIN-oikeudet, muut toiminnot vaativat joko KAYTTAJA-oikeudet tai ei mitään oikeuksia).
- Varauksen tekeminen
- Varausten listaaminen

## Linkki dokumentaatiokansioon
[dokumentaatiota sisaltava kansio](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/tree/master/documentation )


## Linkki kayttotapauksiin
[käyttötarkoituksia-tiedosto](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/dokumentaatio.md )


## Linkki kayttöohjeisiin
[käyttöohje-tiedosto](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kaytto_ohje.md )

## Linkki asennusohjeeseen
[asennusohje-tiedosto](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/asennusohje.md )

## Admin-oikeudet omaava käyttäjä ja kirjautumiseen vaaditut tiedot

| Username | Password |
|:--------:|:--------:|
| hello    |    world |

- Tällä tilillä pystyy käyttämään kaikkia verkkosovelluksen toimintoja

## User-oikeudet omaava käyttäjä ja kirjautumiseen vaaditut tiedot

| Username | Password |
|:--------:|:--------:|
| hei      |   maailma|

- Tällä tilillä pystyy käyttämään kaikkia verkkosovelluksen toimintoja paitsi huoneen lisäystä

## Tämänhetkinen Schema
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Uusin_Schema.png "Nykyinen Schema")







