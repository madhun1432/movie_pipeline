CREATE TABLE movies (
    movieId INTEGER PRIMARY KEY,
    title TEXT,
    year INTEGER,
    genres TEXT,
    director TEXT,
    plot TEXT,
    box_office TEXT
);

CREATE TABLE ratings (
    rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER,
    movieId INTEGER,
    rating FLOAT,
    timestamp BIGINT
);