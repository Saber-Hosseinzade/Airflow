BEGIN TRANSACTION;

DELETE
FROM myschema.inventory
    USING myschema.inventory_staging
WHERE inventory.inventory_id = inventory_staging.inventory_id;

INSERT INTO myschema.inventory
SELECT * FROM myschema.inventory_staging;

END TRANSACTION;