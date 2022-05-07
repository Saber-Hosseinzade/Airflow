BEGIN TRANSACTION;

DELETE
FROM myschema.country
    USING myschema.country_staging
WHERE country.country_id = country_staging.country_id;

INSERT INTO myschema.country
SELECT * FROM myschema.country_staging;

END TRANSACTION;