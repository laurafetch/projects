--Remove existing rows
DELETE FROM inventory;
DELETE FROM shoppings_trip_items;
DELETE FROM shopping_trips;
DELETE FROM locations;
DELETE FROM shopping_list;
DELETE FROM foods;

INSERT INTO foods (name, auto_buy) VALUES
('Milk', TRUE),
('Bread', TRUE),
('Eggs', TRUE),
('Broccoli', FALSE),
('Strawberries', FALSE),
('Bananas', TRUE),
('Turkey meat', FALSE),
('Chicken breast', FALSE);

INSERT INTO shopping_list (food_id, date_added) VALUES
((select id from foods where name = 'Milk'), NOW()),
((select id from foods where name = 'Eggs'), NOW()),
((select id from foods where name = 'Bananas'), NOW());

INSERT INTO locations (location_name) VALUES
('Unknown'),
('Walmart'),
('Giant Eagle'),
('Sams'),
('Aldis');

INSERT INTO shopping_trips (location_id, date) VALUES
((select id from locations where location_name = 'Walmart'), '07/17/2024'),
((select id from locations where location_name = 'Sams'), '07/17/2024');

INSERT INTO shopping_trip_items (shopping_trip_id, food_id, price) VALUES
(1, (select id from foods where name = 'Turkey meat'), 6.99),
(1, (select id from foods where name = 'Broccoli'), 2.99),
(2, (select id from foods where name = 'Strawberries'), 2.99),
(2, (select id from foods where name = 'Bread'), 3.99);

INSERT INTO inventory (food_id, shopping_trip_item_id, in_stock, expiration_date) VALUES
((select id from foods where name = 'Turkey meat'), 1, TRUE, '07/31/2024'),
((select id from foods where name = 'Broccoli'), 2, TRUE, '07/21/2024'),
((select id from foods where name = 'Strawberries'), 3, FALSE, '07/19/2024'),
((select id from foods where name = 'Bread'), 4, TRUE, '07/31/2024');
