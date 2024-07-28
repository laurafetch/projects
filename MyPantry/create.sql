--Create tables
CREATE TABLE foods (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL UNIQUE,
	auto_buy BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE shopping_list (
	id SERIAL PRIMARY KEY,
	food_id INT NOT NULL UNIQUE,
	num_units INT DEFAULT 1,
	date_added DATE NOT NULL
);

CREATE TABLE locations (
	id SERIAL PRIMARY KEY,
	location_name TEXT NOT NULL UNIQUE
);

CREATE TABLE shopping_trips (
	id SERIAL PRIMARY KEY,
	location_id INT NOT NULL,
	date DATE NOT NULL
);

CREATE TABLE shopping_trip_items (
	id SERIAL PRIMARY KEY,
	shopping_trip_id INT NOT NULL,
	food_id INT NOT NULL,
	price FLOAT NOT NULL DEFAULT 0.00
);

CREATE TABLE inventory (
	id SERIAL PRIMARY KEY,
	food_id INT NOT NULL,
	shopping_trip_item_id INT NOT NULL,
	in_stock BOOLEAN NOT NULL,
	expiration_date DATE NOT NULL
);

--Add FKs
ALTER TABLE shopping_list ADD CONSTRAINT fk_shopping_list_food FOREIGN KEY (food_id) REFERENCES foods ON DELETE CASCADE;
ALTER TABLE shopping_trip_items ADD CONSTRAINT fk_shopping_trip_items_food FOREIGN KEY (food_id) REFERENCES foods ON DELETE CASCADE;
ALTER TABLE inventory ADD CONSTRAINT fk_inventory_food FOREIGN KEY (food_id) REFERENCES foods ON DELETE CASCADE;

ALTER TABLE shopping_trips ADD CONSTRAINT fk_shopping_trips_locations FOREIGN KEY (location_id) REFERENCES locations ON DELETE SET NULL;

ALTER TABLE shopping_trip_items ADD CONSTRAINT fk_shopping_trip_items_shopping_trips FOREIGN KEY (shopping_trip_id) REFERENCES shopping_trips ON DELETE SET NULL;

ALTER TABLE inventory ADD CONSTRAINT fk_inventory_shopping_trip_items FOREIGN KEY (shopping_trip_item_id) REFERENCES shopping_trip_items ON DELETE SET NULL;