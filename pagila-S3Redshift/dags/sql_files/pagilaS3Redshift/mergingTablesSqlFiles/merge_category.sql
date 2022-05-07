BEGIN TRANSACTION;

DELETE
FROM myschema.category
    USING myschema.category_staging
WHERE category.category_id = category_staging.category_id;

INSERT INTO myschema.category
SELECT * FROM myschema.category_staging;

END TRANSACTION;