# MyPantry

MyPantry is an application I created to track food inventory, shopping list and shopping trip data.  The goal is to be able to update soon-to-expire items, view my current shopping list, and track shopping trip spending.

## File Description

* create.sql - Contains all scripts needed to recreate the database, along with FKs and indexes
* data.sql - Script to populate tables with test data
* erd.drawio - ERD
* my_pantry.sql - pg_dump of the my_pantry database including test date
* test.sql - Test queries to confirm database schema matches expectations
* insomnia.json - Insomnia export to test endpoints
* my_pantry_flask - Contains code to use Flask-Migrate and Flask to create/maintain database (using ORM) and endpoints (listed below).

## Endpoints

Endpoint | Path | Method(s) | Parameter(s)
---|---|---|---
index|/foods|GET|n/a
shopping_list|/shopping|GET|n/a
add_item|/shopping|POST|food_id INT, num_units INT, date_added DATETIME
remove_item|/shopping/{food_id}|DELETE|n/a
change_num_units|/shopping/{food_id}|PUT|food_id INT, num_units INT

## Description
The application has a lot of potential.  The original schema design highlights that potential.  Throughout the development, the decision was made to focus on the shopping list.  That one piece is able to show off all the features of this project.  It can utilize all endpoint methods.  Additionally, this piece is essential for adding more complexity to the project.

## Enhancements

The project doesn't include the full potential of the database.  Some future enhancements are adding database triggers to automatically update the inventory table and remove items from the shopping list table.  Additionally, creating some functions in either the database or python to pull more information regarding shopping trip trends.
