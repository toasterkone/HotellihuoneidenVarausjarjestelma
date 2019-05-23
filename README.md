
# VarausApp

# Tietokantasovellus-kurssi

## Linkki Herokussa sijaitsevaan sovellukseen
(https://tsoha-varaussovellus.herokuapp.com/ "Herokussa oleva sovellus")

(https://tsoha-varaussovellus.herokuapp.com/)

## HotellihuoneidenVarausjarjestelma

## Aihe
- Hotellien varausjärjestelmä

## Aihekuvaus

Hotellien varausjärjestelmä sisältää huoneita halutun määrän ja huoneita voidaan lisätä halutessa. Huoneita voidaan varata ja huoneille voidaan ostaa lisavarusteita. Huoneita on eri hintaisia ja tyyppisiä. Varauksia voidaan perua. Varausjärjestelmä sisältää alustavasti neljä tietokantataulua: asiakas, hotellihuone, lisavaruste ja varaus. Hotellihuoneet varataan aina viikko kerrallaan ja varausajoista pidetään kirjaa viikkonumeroiden avulla.

Asiakkaasta tallennetaan ainakin etu- ja sukunimi, puhelinnumero, sähköposti. Hotellihuoneella on huonenumero, hinta, tyyppi. Lisävarusteella on hinta, nimi ja tieto mihin varaukseen se liittyy.

Huoneen varausta varten pitää asiakkaan maksaa varausmaksu, joka riippuu huoneesta. 


## Tietokantataulut
- Asiakas
- Hotellihuone 
- Lisavaruste
- Varaus

## Tietokantakaavion kuvaus
- Asiakas((PK) id:Integer, etunimi:Varchar, sukunimi:Varchar, puhelinnumero:Varchar, email:Varchar)
- Varaus((PK) id:Integer, (FK) asiakas_id:Asiakas, (FK) hotellihuone_id:Hotellihuone, varausviikko:Integer, hinta:Integer)
- Hotellihuone((PK) id:Integer, (FK) varaus_id:Varaus, huonenumero:Integer, hinta:Integer, tyyppi:Varchar)
- Lisavaruste((PK) id:Integer, (FK) varaus_id:Varaus, hinta:Integer, nimi:Varchar)

## Kuva tietokantakaaviosta
![alt text](https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/blob/master/v_2.png "Tietokantakaavio")

## Toiminnot

- kirjautuminen
- Lisaa huone
- listaa huoneet
- listaa asiakkaat
- listaa varaukset
- tee varaus
- peru varaus
- lisävarusteen osto

## Linkki kayttotapauksiin
(https://github.com/toasterkone/HotellihuoneidenVarausjarjestelma/tree/master/documentation "kansio sisaltaa kayttotapaukse")



