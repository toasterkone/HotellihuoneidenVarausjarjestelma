# VarausApp - Alustava Käyttöohje

Sovellusta voi käyttää nettiosoitteessa [https://tsoha-varaussovellus.herokuapp.com/](https://tsoha-varaussovellus.herokuapp.com/) tai jos sovelluksen asentaa lokaalisti niin osoitteessa [http://localhost:5000/](http://localhost:5000/).

- Lokaalin asennuksen ohjeet tiedostossa asennusohje.md


## Tämä dokumentti sisältää ohjeet seuraavia toiminnallisuuksia varten
- Kirjautuminen
- Rekisteröityminen
- Asiakkaan lisääminen, poistaminen, tietojen muokkaus ja asiakkaiden listaus
- Lisää huone
- Listaa huoneet
- Lisää varaus
- Listaa varaukset
- Peru varaus
- Uloskirjautuminen

## Aloitussivu - kirjautumattomana

![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Aloitussivu_kirjautumaton.png "Kuva aloitussivusta kirjautumattomana")

Siirtyessäsi yllä olevalle sovellussivulle sinulle avautuu yllä olevan kuvan mukainen näkymä. Sivun yläreunassa näkyvät sovelluksen toiminnallisuudet. Tietyt toiminnallisuudet vaativat kirjautumisen joko käyttäjänä tai adminina.

## Aloitussivu - Käyttäjänä kirjautuneena

![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Aloitussivu_k%C3%A4ytt%C3%A4j%C3%A4.png "Kuva aloitussivusta käyttäjänä kirjautuneena")

Siirtyessäsi yllä olevalle sovellussivulle sinulle avautuu yllä olevan kuvan mukainen näkymä. Sivun yläreunassa näkyvät sovelluksen toiminnallisuudet. Pystyt käyttämään kaikkia toiminnallisuuksia paitsi huoneen lisäystä.

## Aloitussivu - Adminina kirjautuneena

![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Aloitussivu_Admin.png "Kuva aloitussivusta adminina kirjautuneena")

Siirtyessäsi yllä olevalle sovellussivulle sinulle avautuu yllä olevan kuvan mukainen näkymä. Sivun yläreunassa näkyvät sovelluksen toiminnallisuudet. Aloitussivulla näytetään myös käyttäjät, joilla ei ole yhtään asiakasta (näkyy vain, jos kirjautunut adminina). Pystyt käyttämään kaikkia toiminnallisuuksia. 


## Kirjautuminen

![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Kirjautuminen_sivu.png "Kuva kirjautumissivusta")


Sovellukseen pääsee muutkin kuin kirjautuneet, mutta tietyt toiminnallisuudet, kuten asiakkaan ja huoneen lisäys vaativat kirjautumisen. Listaavat toiminnallisuudet eivät tarvitse kirjautumista. Sovelluksessa on kahta eri tyyppiä käyttäjätilien suhteen: admin-oikeudet omaava tili, joka pystyy lisäämään huoneen ja käyttäjä-oikeudet omaava tili, joka pystyy tekemään kaiken muun paitsi lisäämään huoneen. Herokussa sijaitsevassa sovelluksessa on valmiina admin- ja käyttäjä-tilit, joiden tiedot ovat seuraavat:

- admin-oikeudet omaava tili

| Username | Password |
|:--------:|:--------:|
| hello    |    world |

- käyttäjä-oikeudet omaava tili

| Username | Password |
|:--------:|:--------:|
| hei      |   maailma|

Kirjautuminen tapahtuu sivun oikean yläreunan "Kirjaudu"-linkkiä painamalla ja uloskirjautuminen tapahtuu "Kirjaudu ulos"-linkkiä painamalla.

## Rekisteröityminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/rekisteroityminen.png "Rekisteröitymissivu")

Sovelluksessa on mahdollista rekisteröityä aloitussivun oikean ylänurkan "Rekisteröidy"-linnkiä painamalla. Linkkiä seuraa lomake, jossa kysytään nimi, käyttäjätunnus ja salasana. Kaikkien näiden pitää olla minimissään 2 merkkiä ja maksimissaan 144 merkkiä pitkiä. Rekisteröityminen ohjaa automaattisesti kirjautumissivulle. 

- Huom! Kun rekisteröidyt niin sinulla on vain käyttäjä-tilin oikeudet, eli et pysty lisäämään huoneita.


## Asiakkaiden listaaminen, tietojen muuttaminen ja asiakkaan poistaminen (CRUD)
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Listaa_asiakkaat.png "CRUD: Asiakkaiden listaaminen, muokkaaminen ja poistaminen")

- Asiakkaan poistaminen ja asiakkaan tietojen muokkaaminen vaatii kirjautumisen. Kuka vaan voi nähdä asiakkaiden listauksen.

- Asiakkaiden listaaminen

Aloitussivun "Listaa Asiakkaat"-linkkiä painamalla avautuu näkymä, jossa listataan kaikki asiakkaat.

- Asiakkaan tietojen muokkaaminen

Asiakkaiden listaus-sivulla sijaitsee muokkaa-nappi, jota painaminen kirjautuneena vie lomakkeelle, joka on alla kuvassa. Tässä voi kirjoittaa päivitetyt tiedot ja painaa päivitä asiakkaan tiedot -nappia, jolloin asiakkaan tiedot päivittyvät.

![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Listaa_asiakkaat.png "Asiakkaan tietojen päivittäminen")

- Asiakkaan poistaminen

Asiakkaan poistaminen tapahtuu painamalla punaista delete-nappia poistettavaksi halutun asiakkaan rivin kohdalla. Tämä toiminto vaatii kirjautumisen.


## Asiakkaan lisääminen (CRUD)

![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Lis%C3%A4%C3%A4_asiakas.png "Lomake, jolla asiakas lisätään.")

Asiakkaan lisääminen vaatii kirjautumisen ja aloitussivun yläreunan "Lisää asiakas"-linkin painamisen. Lisäämissivulla pitää määrittää asiakkaan etunimi, sukunimi, puhelinnumero ja sähköpostiosoite. Etu- ja sukunimen pitää olla vähintään 2 merkkiä pitkiä. Puhelinnumeron pitää olla vähintään 5 merkkiä pitkä. Sähköpostin pitää olla vähintään 3 merkkiä pitkä. Asiakkaan lisäys tapahtuu tietojen lisäyksen jälkeen painamalla "Lisää uusi asiakas"-painiketta. 


## Huoneen lisääminen

![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Lis%C3%A4%C3%A4_huone.png "Lomake, jolla huone lisätään.")

- Aloitussivun linkkiä "Lisää huone" painamalla avautuu huoneen lisäämisnäkymä, jos on kirjautunut admin-oikeuksilla. Jos et ole tehnyt tätä, niin sinut ohjataan automaattisesti kirjautumissivulle.

- Huoneen lisäys onnistuu lomakkeella, johon syötetään huonenumero (kokonaisluku, joka vähintään 1), huoneen hinta (kokonaisluku, joka vähintään 1) ja huoneen tyyppi (merkkijono, joka vähintään 3 merkkiä pitkä).

## Huoneiden listaaminen

![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Listaa_huoneet.png "Huoneiden listaus, huonenumero, hinta, tyyppi")

- Aloitussivun "Listaa huoneet"-linkkiä painamalla pääsee näkymään, jossa näytetään lisätyt huoneet. Huoneet listataan riveittäin siten, että ensin on huonenumero, toiseksi huoneen hinta ja viimeiseksi huoneen tyyppi.

## Varauksen tekeminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Varauksen_tekeminen.png "Lomake, jolla varaus lisätään.")

- Sivun yläosan "Lisää varaus"-linkkiä painamalla (kirjautuneena) voi tehdä varauksen. Syötä huone_id, asiakas_id, varausviikko ja hinta. Voit nähdä tarvittavat id:t ja hinnat sovelluksen sivuilta "Listaa huoneet" ja "Listaa asiakkaat".
- Huom! Varaus tehdään kokonaiselle viikolle käyttäen viikkonumeroita. Voit varata huoneen viikoksi kerrallaan.

## Varausten listaaminen

![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Listaa_varaukset.png "Varausten listaaminen")

- Aloitussivun "Listaa varaukset"-linkkiä painamalla pääsee näkymään, jossa näytetään lisätyt varaukset.
- Voit tarkastaa tästä, onko haluamasi huone vapaana haluttuun aikaan.

## Varauksen peruminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Listaa_varaukset.png "varauksen peruminen")

- Aloitussivun "Listaa varaukset"-linkkiä painamalla pääseen näkymään, jossa näytetään lisätyt varaukset. Tässä näkymässä voi perua halutun varauksen painamalla kyseisen varauksen rivin kohdalla olevaa punaista nappia, jossa lukee "peru varaus". Tämä toiminto vaatii kirjautumisen.

## Uloskirjautuminen

Uloskirjautuminen tapahtuu painamalla sivuston oikean ylänurkan "Kirjaudu ulos"-linkkiä. Tämä kirjaa käyttäjän automaattisesti ulos.






