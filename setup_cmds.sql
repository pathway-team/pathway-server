CREATE DATABASE pathwaydb;
/*Make sure to update this for production
 to be actually secure.*/
CREATE USER django WITH PASSWORD 'password';

ALTER ROLE django SET client_encoding TO 'utf8';
ALTER ROLE django SET default_transaction_isolation TO 'read committed';
ALTER ROLE django SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE pathwaydb TO django;
