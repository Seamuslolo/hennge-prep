CREATE TABLE movies(
    id INTEGER PRIMARY KEY,
    title varchar(100) NOT NULL,
    rating INTEGER,
    constraint rating_range check(
        rating >= 0 AND rating < 11
    )
);

    rating Integer,
    CONSTRAINT rating_range CHECK(
        rating >= 0 AND rating rating < 11
    )

INSERT INTO movies(title, rating)
VALUES 
    ('the white house', 10),
    ('three little pig', 8),
    ('the big fox', 9),
    ('the dawn wall', 5);

SELECT id, title, rating FROM movies 
WHERE rating >= 8
ORDER BY rating DESC;


