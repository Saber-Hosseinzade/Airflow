BEGIN TRANSACTION;

DELETE
FROM myschema.store
    USING myschema.store_staging
WHERE store.store_id = store_staging.store_id;

INSERT INTO myschema.store
SELECT * FROM myschema.store_staging;

END TRANSACTION;