# VarausApp 
- Tämä tiedosto sisältää sovelluksen toteutuneet/toteutumattomat ominaisuudet ja jatkokehitysideoita

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
- Tuotannossa käytössä PSQL ja lokaalisti SQLite

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
- Lisää erilaisia yhteenvetokyselyitä ja muita kyselyitä
