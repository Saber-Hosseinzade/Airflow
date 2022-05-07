BEGIN TRANSACTION;

DELETE
FROM myschema.film_category
    USING myschema.film_category_staging
WHERE film_category.film_id = film_category_staging.film_id
AND film_category.category_id = film_category_staging.category_id;

INSERT INTO myschema.film_category
SELECT * FROM myschema.film_category_staging;

END TRANSACTION;