BEGIN TRANSACTION;

DELETE
FROM myschema.actor
    USING myschema.actor_staging
WHERE actor.actor_id = actor_staging.actor_id;

INSERT INTO myschema.actor
SELECT * FROM myschema.actor_staging;

END TRANSACTION;