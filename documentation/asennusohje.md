# Tietokantasovelluksen asentaminen lokaalisti omalle tietokoneelle

- Huom! Sovellus on tarkoitettu asennettavaksi Linux-käyttöjärjestelmälle. Muilla käyttöjärjestelmillä asentaminen voi johtaa virheisiin.

## Sovelluksen asentamisen aloittamisen vaatimat ohjelmistot

- Python (vähintään versio 3.5).
- Tuki Python-kirjastojen lataamiseen (Pythonin pip).
- Tuki Python-"virtuaaliympäristöjen" luomiseen (Pythonin venv-kirjasto).
- SQLite3-tietokannanhallintajärjestelmä (tietokantaa käytetään lokaalisti tällä).

## Sovelluksen asentaminen lokaalisti

1. Varmista, että ylläolevat ohjelmistot ovat asennettu ja käytössä Linux-käyttöjärjestelmä.

2. Mene komentorivillä siihen kansioon, johon haluat kloonata projektin. Syötä komentoriviin seuraava komento, jotta projekti kloonautuu githubista: [https://github.com/toasterkone](https://github.com/toasterkone)

```
git clone git@github.com:toasterkone/HotellihuoneidenVarausjarjestelma.git
```

3. Virtuaaliympäristön luominen 

```
python3 -m venv venv
```

4. Aktivoi virtuaaliympäristö

```
source venv/bin/activate
```

5. Sovelluksen tiedoston requirements.txt riippuvuuksien asentaminen

```
pip install -r requirements.txt
```

6. Sovelluksen käynnistäminen lokaalisti

```
python3 run.py
```

7. Sovellus on nyt asennettu lokaalisti ja käynnistetty

## Sovelluksen käyttäminen asentamisen jälkeen (jatka edellisestä kohdasta 7.)

1. Syötä ensin tietokantaan tarvittavat roolit (ADMIN ja KAYTTAJA) antamalla seuraavat komennot kometorivissä

```
INSERT INTO rooli (nimi) VALUES ('ADMIN');
```

```
INSERT INTO rooli (nimi) VALUES ('KAYTTAJA');
```

Nyt tietokannassa on kaksi roolia: admin ja käyttäjä.

2. Syötä tietokantaan ensimmäinen admin-käyttäjä

```
INSERT INTO account (name, username, password, rooli_id) VALUES ('Admini', 'Admin', 'salasana123', 1);
```

HUOM! Voit vaihtaa kohtiin name, username ja password haluamasi merkkijonot, mutta viimeisenä syötettävän numeron on oltava yksi, jotta käyttäjä omaa admin-oikeudet.

3. Varmista, että admin-oikeudet omaava käyttäjä on lisätty

```
SELECT * FROM account;
```

Tässä pitäisi näkyä äsken lisätty käyttäjä, jolla on rooli_id:n arvo 1.

4. Siirry verkkosivulle

- [http://localhost:5000/](http://localhost:5000/)

5. Nyt voit käyttää kaytto_ohje.md-tiedoston mukaisesti sovellusta 

Voit aloittaa esimerkiksi rekisteröitymällä (tämä lisää käyttäjä-oideudet omaavan tilin).

Huom! Käytössä on nyt aiemmin luotu admin-oikeudet omaava tili, eli voit kirjautua sillä.

## Herokuun asentaminen

1. Varmista, että olet asentanut ensin sovelluksen lokaalisti yllä olevan ohjeen mukaisesti.

2. Asenna Herokun työväline 

Löytyy osoitteesta: [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

```
sudo snap install --classic heroku
```

3. Varmista, että olet sovelluskansiossa ja syötä seuraava käsky

```
source venv/bin/activate
```

4. Luo sovellukselle paikka Herokuun

```
heroku create SOVELLUSNIMI
```

- Missä "SOVELLUSNIMI" on haluttu nimi sovellukselle

5. Lisää tieto Herokusta paikalliseen versionhallintaan

```
git remote add heroku 
```

6. Lähetä projekti Herokuun

```
git add .
git commit -m "Initial commit"
git push heroku master
```

7. Sovellus on nyt toiminnassa Herokussa

8. Lisää sovelluksen käyttöön tieto siitä, että se on Herokussa

```
heroku confic:set HEROKU=1
```

9. Lisää herokuun tietokanta

```
heroku addons:add heroku-postgresql:hobby-dev
```

10. Herokussa on nyt sovellukselle postgresql-tietokanta

11. Lisää tietokantaan roolit ja admin-käyttäjä

```
heroku pg:psql
```

- toista ylemmän ohjeen " Sovelluksen käyttäminen asentamisen jälkeen (jatka edellisestä kohdasta 7.)" kohdat 1-3. 

12. Nyt voit käyttää sovellusta Herokun kautta ja tehdä esimerkiksi kaytto_ohje.md-tiedoston mukaisia tehtäviä


  
