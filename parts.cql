CREATE KEYSPACE store
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};

CREATE TABLE demo.users (
    id text PRIMARY KEY,
    part text,
    customer text,
    retailer text,
    price int);

      