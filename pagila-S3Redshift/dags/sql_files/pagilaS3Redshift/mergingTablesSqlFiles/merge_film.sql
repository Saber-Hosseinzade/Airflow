BEGIN TRANSACTION;

DELETE
FROM myschema.film
    USING myschema.film_staging
WHERE film.film_id = film_staging.film_id;

INSERT INTO myschema.film
SELECT * FROM myschema.film_staging;

END TRANSACTION;