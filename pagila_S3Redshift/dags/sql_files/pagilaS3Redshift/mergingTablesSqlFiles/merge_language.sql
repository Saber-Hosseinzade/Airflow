BEGIN TRANSACTION;

DELETE
FROM myschema.language
    USING myschema.language_staging
WHERE language.language_id = language_staging.language_id;

INSERT INTO myschema.language
SELECT * FROM myschema.language_staging;

END TRANSACTION;