# VarausApp - Alustava Käyttöohje

Sovellusta voi käyttää nettiosoitteessa [https://tsoha-varaussovellus.herokuapp.com/](https://tsoha-varaussovellus.herokuapp.com/) tai jos sovelluksen asentaa lokaalisti niin osoitteessa [http://localhost:5000/](http://localhost:5000/).

- Lokaalin asennuksen ohjeet tiedostossa asennusohje.md


## Aloitussivu

Siirtyessäsi yllä olevalle sovellussivulle sinulle avautuu alla olevan kuvan mukainen näkymä. Sivun yläreunassa näkyvät sovelluksen toiminnallisuudet. Aloitussivulla näytetään myös käyttäjät, joilla ei ole yhtään asiakasta. 

![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Aloitus_sivu.png "Kuva aloitussivusta")


## Kirjautuminen

Sovellukseen pääsee muutkin kuin kirjautuneet, mutta tietyt toiminnallisuudet, kuten asiakkaan ja huoneen lisäys vaativat kirjautumisen. Listaavat toiminnallisuudet eivät tarvitse kirjautumista. Sovelluksessa on kahta eri tyyppiä käyttäjätilien suhteen: admin-oikeudet omaava tili, joka pystyy lisäämään huoneen ja käyttäjä-oikeudet omaava tili, joka pystyy tekemään kaiken muun paitsi lisäämään huoneen. Herokussa sijaitsevassa sovelluksessa on valmiina admin- ja käyttäjä-tilit, joiden tiedot ovat seuraavat:


| Username | Password |
|:--------:|:--------:|
| hello    |    world |

- admin-oikeudet omaava tili

| Username | Password |
|:--------:|:--------:|
| hei      |   maailma|

- käyttäjä-oikeudet omaava tili

Kirjautuminen tapahtuu sivun oikean yläreunan "Kirjaudu"-linkkiä painamalla ja uloskirjautuminen tapahtuu "Kirjaudu ulos"-linkkiä painamalla.

## Rekisteröityminen

Sovelluksessa on mahdollista rekisteröityä aloitussivun oikean ylänurkan "Rekisteröidy"-linnkiä painamalla. Linkkiä seuraa lomake, jossa kysytään nimi, käyttäjätunnus ja salasana. Kaikkien näiden pitää olla minimissään 2 merkkiä ja maksimissaan 144 merkkiä pitkiä. Rekisteröityminen ohjaa automaattisesti kirjautumissivulle. 

- Huom! Kun rekisteröidyt niin sinulla on vain käyttäjä-tilin oikeudet, eli et pysty lisäämään huoneita.


## Asiakkaiden listaaminen, tietojen muuttaminen ja asiakkaan poistaminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Asiakkaiden%20listaaminen%20ja%20poistaminen.png "Asiakkaiden listaaminen, muokkaaminen ja poistaminen")


- Asiakkaan poistaminen vaatii kirjautumisen. Käyttäjä voi muokata ja poistaa asiakkaan. Kuka vaan voi nähdä asiakkaiden listauksen.

- Asiakkaiden listaaminen

Aloitussivun "Listaa Asiakkaat"-linkkiä painamalla avautuu näkymä, jossa listataan kaikki asiakkaat. Tietojen järjestys on seuraava: etunimi, sukunimi, puhelinnumero ja sähköpostiosoite.

- Asiakkaan tietojen muokkaaminen

Voit muuttaa vain yhden asiakkaan yhtä tietoa kerrallaan. Esimerkiksi haluttaessa vaihtaa asiakkaan puhelinnumeroa pitää syöttää uusi numero kolmanteen tekstikenttään ja painaa sen alla olevaa "Vaihda puh.num."-painiketta. Tämä muuttaa asiakkaan puhelinnumeron. Saman voi tehdä muille tiedoille.

- Asiakkaan poistaminen

Asiakkaan poistaminen tapahtuu painamalla punaista delete-nappia poistettavaksi halutun asiakkaan rivin kohdalla. Tämä toiminto vaatii kirjautumisen.


## Asiakkaan lisääminen

![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/asiakkaan%20lisaaminen.png "Lomake, jolla asiakas lisätään.")

Asiakkaan lisääminen vaatii kirjautumisen ja aloitussivun yläreunan "Lisää asiakas"-linkin painamisen. Lisäämissivulla pitää määrittää asiakkaan etunimi, sukunimi, puhelinnumero ja sähköpostiosoite. Etu- ja sukunimen pitää olla vähintään 2 merkkiä pitkiä. Puhelinnumeron pitää olla vähintään 5 merkkiä pitkä. Sähköpostin pitää olla vähintään 3 merkkiä pitkä. Asiakkaan lisäys tapahtuu tietojen lisäyksen jälkeen painamalla "Lisää uusi asiakas"-painiketta. 


## Huoneiden listaaminen

![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Huoneiden_listaaminen.png "Huoneiden listaus, huonenumero, hinta, tyyppi")

- Aloitussivun "Listaa huoneet"-linkkiä painamalla pääsee näkymään, jossa näytetään lisätyt huoneet. Huoneet listataan riveittäin siten, että ensin on huonenumero, toiseksi huoneen hinta ja viimeiseksi huoneen tyyppi.

## Huoneen lisääminen

![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Huoneen_lisaaminen.png "Lomake, jolla huone lisätään.")

- Aloitussivun linkkiä "Lisää huone" painamalla avautuu huoneen lisäämisnäkymä, jos on kirjautunut admin-oikeuksilla. Jos et ole tehnyt tätä, niin sinut ohjataan automaattisesti kirjautumissivulle.

- Huoneen lisäys onnistuu lomakkeella, johon syötetään huonenumero (kokonaisluku, joka vähintään 1), huoneen hinta (kokonaisluku, joka vähintään 1) ja huoneen tyyppi (merkkijono, joka vähintään 3 merkkiä pitkä).

## Varauksen tekeminen
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Huoneen_lisaaminen.png "Lomake, jolla varaus lisätään.")

- Sivun yläosan "Lisää varaus"-linkkiä painamalla (kirjautuneena) voi tehdä varauksen. Syötä huone_id, asiakas_id, varausviikko ja hinta. Voit nähdä tarvittavat id:t ja hinnat sovelluksen sivuilta "Listaa huoneet" ja "Listaa asiakkaat".
- Huom! Varaus tehdään kokonaiselle viikolle käyttäen viikkonumeroita. Voit varata huoneen viikoksi kerrallaan.

## Varausten listaaminen

![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/documentation/kayttotarkoituskuvia/Huoneiden_listaaminen.png "Varausten listaaminen")

- Aloitussivun "Listaa varaukset"-linkkiä painamalla pääsee näkymään, jossa näytetään lisätyt varaukset.
- Voit tarkastaa tästä, onko haluamasi huone vapaana haluttuun aikaan.

## Uloskirjautuminen

Uloskirjautuminen tapahtuu painamalla sivuston oikean ylänurkan "Kirjaudu ulos"-linnkiä. Tämä kirjaa käyttäjän automaattisesti ulos.






