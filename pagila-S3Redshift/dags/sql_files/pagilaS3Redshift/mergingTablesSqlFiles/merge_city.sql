BEGIN TRANSACTION;

DELETE
FROM myschema.city
    USING myschema.city_staging
WHERE city.city_id = city_staging.city_id;

INSERT INTO myschema.city
SELECT * FROM myschema.city_staging;

END TRANSACTION;