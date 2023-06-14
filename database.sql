CREATE TABLE categories (
            id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            name varchar(255),
            created_at DATE );


CREATE TABLE currencies (
            id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            name varchar(255),
            created_at DATE );


CREATE TABLE expenses (
            id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            name varchar(255),
            sum FLOAT,
            currency BIGINT REFERENCES categories (id),
            date DATE,
            category BIGINT REFERENCES categories (id),
            created_at DATE );
