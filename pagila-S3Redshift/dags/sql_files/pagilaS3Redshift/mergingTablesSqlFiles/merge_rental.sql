BEGIN TRANSACTION;

DELETE
FROM myschema.rental
    USING myschema.rental_staging
WHERE rental.rental_id = rental_staging.rental_id;

INSERT INTO myschema.rental
SELECT * FROM myschema.rental_staging;

END TRANSACTION;