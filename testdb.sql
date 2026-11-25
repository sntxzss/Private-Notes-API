DROP TABLE IF EXISTS cities;
CREATE TABLE cities (name text, region text,
                     population integer, founded integer);
INSERT INTO cities VALUES
    ('Київ', 'Київська', 2952000, 482),
    ('Львів', 'Львівська', 717000, 1256),
    ('Одеса', 'Одеська', 1010000, 1794),
    ('Харків', 'Харківська', 1421000, 1654),
    ('Біла Церква', 'Київська', 207000, 1032),
    ('Ужгород', 'Закарпатська', 115000, NULL); -- NULL: «невідомо»
-- 1. Усі міста від найбільшого
SELECT name, population FROM cities ORDER BY population DESC;
-- 2. Міста Київської області
SELECT name FROM cities WHERE region = 'Київська';
-- 3. Населення від 500 тис. до 1,5 млн (межі включно)
SELECT name FROM cities WHERE population BETWEEN 500000 AND 1500000;
-- 4. Назва починається на «Л» або «О»
SELECT name FROM cities WHERE name LIKE 'Л%' OR name LIKE 'О%';
-- 5. Рік заснування невідомий
SELECT name FROM cities WHERE founded IS NULL;
-- 6. Унікальні області за алфавітом
SELECT DISTINCT region FROM cities ORDER BY region;
-- 7. Друга «сторінка» по 2 міста за населенням
