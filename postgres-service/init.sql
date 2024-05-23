CREATE USER envoy WITH PASSWORD 'envoy';
CREATE DATABASE envoy;
GRANT ALL PRIVILEGES ON DATABASE envoy TO envoy;

\c envoy;

CREATE TABLE cars (
  brand VARCHAR(255),
  model VARCHAR(255),
  year INT
);

GRANT ALL PRIVILEGES ON TABLE cars TO envoy;

INSERT INTO cars VALUES ('Audi',	'A6',		1998);
INSERT INTO cars VALUES ('Peugeot',	'206',		2006);
INSERT INTO cars VALUES ('Renault',	'Captur',	2018);
