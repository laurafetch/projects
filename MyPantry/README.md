# MyPantry

MyPantry is an application I created to track food inventory, shopping list and shopping trip data.  The goal is to be able to update soon-to-expire items, view my current shopping list, and track shopping trip spending.

## File Description

* create.sql - Contains all scripts needed to recreate the database, along with FKs and indexes
* data.sql - Script to populate tables with test data
* erd.drawio - ERD
* my_pantry.sql - pg_dump of the my_pantry database including test date
* test.sql - Test queries to confirm database schema matches expectations

## Endpoints

Endpoint | Path | Method(s) | Parameter(s)
---|---|---|---
index|/foods|GET|n/a
shopping_list|/shopping|GET|n/a
add_item|/shopping|POST|food_id INT, num_units INT, date_added DATETIME
remove_item|/shopping/{food_id}|DELETE|n/a
change_num_units|/shopping/{food_id}|PUT|food_id INT, num_units INT
