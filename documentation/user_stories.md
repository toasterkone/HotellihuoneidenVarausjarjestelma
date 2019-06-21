# VarausApp - Käyttötapaukset
- Tässä dokumentissa on kuvattuna sovelluksen oleellisia käyttötapauksia suunnitelluille käyttäjäryhmille (hotellin työntekijät ja omistaja). Sisältää myös liittyvät SQL-kyselyt.

## Hotellin työntekijä (KÄYTTÄJÄ-oikeudet)

1. Tehdään uudelle asiakkaalle varaus. Asiakas on soittanut, kertonut yhteystiedot, kertonut minkälaisen huoneen haluaa ja mille viikolle.

- Syötetään uusi asiakas tietokantaan
```
INSERT INTO asiakas (etunimi, sukunimi, puhelinnumero, email) VALUES ('Matti', 'Meikäläinen', '0501234567', 'matti.meikalainen@aol.com');
```
jossa VALUES () sulkeiden sisälle asiakkaan tiedot.

- Tehdään varaus halutulle huoneelle
```
INSERT INTO varaus (varausviikko, huone_id, asiakas_id, hinta) VALUES (14, 1, 1, 25);
```
jossa VALUES () sulkeiden sisällä asiakkaan haluaman tyyppisen huoneen id, haluttu viikkonumero, asiakkaan id ja huoneen hinta.

Tätä varten työntekijän pitää tarkistaa "Listaa huoneet" ja "Listaa varaukset" -linkeistä, että sopivia huoneita on vapaana haluttuun aikaan. Myös asiakkaan id pitää varmistaa linkistä "Listaa asiakkaat".

2. Edelliseen tehtävään liittyen tarvitsee tietää vapaat huoneet haluttuna viikkona.

```
SELECT huone.id
FROM huone
LEFT JOIN varaus ON huone.id = varaus.huone_id
WHERE huone.tyyppi = 'haluttuTyyppi' AND varaus.varausviikko NOT IN (123);
```
jossa 'haluttuTyyppi' on asiakkaan toivoma huonetyyppi ja 123 on haluttu viikkonumero. Kysely palauttaa sopivat vapaat huoneet.


3. Jokin asiakkaan tiedoista on kirjattu väärin, joten se pitää päivittää.

```
UPDATE asiakas
SET etunimi = 'oikea etunimi', sukunimi = 'oikea sukunimi', puhelinnumero = 'oikea puhelinnumero', email = 'oikea email'
WHERE id = 123;
```
jossa id on asiakkaan identifioiva pääavain ja SET-komentoa seuraavat tiedot ovat oikeat tiedot.

4. Asiakas haluaa poistaa tietonsa hotellin tietojärjestelmistä.
```
DELETE FROM asiakas
WHERE id = 123;
```
jossa id on poistettavan asiakkaan pääavain.

5. Haluan listata kaikki asiakkaat.
```
SELECT * FROM asiakas;
```


6. Haluan listata kaikki huoneet.
```
SELECT * FROM huone;
```

7. Haluan listata kaikki varaukset.
```
SELECT * FROM varaus;
```

8. Haluan poistaa asiakkaan peruman varauksen
```
DELETE FROM varaus
WHERE id = 123;
```
jossa id on peruttavan varauksen id.

## Hotellinomistaja (ADMIN-oikeudet)
- Pystyn tekemään kaikki yllä mainitut tehtävät.


1. Haluan nähdä ketkä työntekijät eivät ole lisänneet asiakkaita.
```
SELECT Account.id, Account.name 
FROM Account
LEFT JOIN Asiakas ON Asiakas.account_id = Account.id
WHERE Asiakas.id IS NULL
GROUP BY Account.id
HAVING COUNT(Asiakas.id) = 0;
```
2. Haluan lisätä hotellin laajennuksen seurauksena uuden huoneen.

```
INSERT INTO huone (huonenumero, hinta, tyyppi) VALUES (123, 456, 'huoneTyyppi');
``` 
jossa 123 on uuden huoneen huonenumero, 456 on huoneen hinta ja 'huoneTyyppi' on huoneen tyyppi.


