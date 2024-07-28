--Test fake data
--Confirm all records
SELECT * FROM foods;
SELECT * FROM shopping_list;
SELECT * FROM locations;
SELECT * FROM shopping_trips;
SELECT * FROM shopping_trip_items;
SELECT * FROM inventory;

--Current shopping list
SELECT f.name, sl.num_units, sl.date_added
FROM shopping_list as sl
INNER JOIN foods as f 
on sl.food_id = f.id;

--Current pantry
SELECT f.name, count(*) as number_of_units
FROM inventory as i 
INNER JOIN foods as f 
on i.food_id = f.id
WHERE i.in_stock = TRUE
GROUP BY f.name;

--Soon to expire
SELECT f.name, i.expiration_date
FROM inventory as i 
INNER JOIN foods as f 
on i.food_id = f.id
WHERE i.in_stock = TRUE
AND i.expiration_date <= NOW() + interval '7' day;

--Spending stats
SELECT f.name, AVG(sti.price), l.location_name
FROM shopping_trip_items As sti 
INNER JOIN shopping_trips AS st 
ON sti.shopping_trip_id = st.id 
INNER JOIN locations AS l 
ON st.location_id = l.id
INNER JOIN foods as f 
on sti.food_id = f.id
GROUP BY f.name, l.location_name;