BEGIN TRANSACTION;

DELETE
FROM myschema.film_actor
    USING myschema.film_actor_staging
WHERE film_actor.film_id = film_actor_staging.film_id
AND film_actor.actor_id = film_actor_staging.actor_id;

INSERT INTO myschema.film_actor
SELECT * FROM myschema.film_actor_staging;

END TRANSACTION;