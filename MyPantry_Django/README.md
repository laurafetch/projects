# MyPantry

MyPantry is an application I created to track food inventory, shopping list and shopping trip data.  The goal is to be able to update soon-to-expire items, view my current shopping list, and track shopping trip spending.

This version of the application was created to using Django and Docker.  It is focuses on pulling the current inventory and shopping list.  The app has endpoints to add, update, and remove items from the shopping list as well.


## Endpoints

Endpoint | Path | Method(s) | Parameter(s)
---|---|---|---
inventory|/foods|GET|n/a
shopping_list|/shopping|GET|n/a
add_item|/shopping|POST|food_id INT, num_units INT, date_added DATETIME
remove_item|/shopping/{food_id}|DELETE|n/a
edit_item|/shopping/{food_id}|PATCH|food_id INT, num_units INT

## Description

The application builds upon the same application I created using Flask.  This expands into Django, introduces html files, Dockerfile and Docker Compose.  Additionally, I deployed the application to Google Cloud.  Intructions and screenshots are in the deployment_gcp folder.


## Enhancements

The project doesn't include the full potential of the database.  Some future enhancements are adding database triggers to automatically update the inventory table and remove items from the shopping list table.  Additionally, creating some functions in either the database or python to pull more information regarding shopping trip trends.
