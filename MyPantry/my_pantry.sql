--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: foods; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.foods (
    id integer NOT NULL,
    name text NOT NULL,
    auto_buy boolean DEFAULT false NOT NULL
);


ALTER TABLE public.foods OWNER TO postgres;

--
-- Name: foods_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.foods_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.foods_id_seq OWNER TO postgres;

--
-- Name: foods_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.foods_id_seq OWNED BY public.foods.id;


--
-- Name: inventory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.inventory (
    id integer NOT NULL,
    food_id integer NOT NULL,
    shopping_trip_item_id integer NOT NULL,
    in_stock boolean NOT NULL,
    expiration_date date NOT NULL
);


ALTER TABLE public.inventory OWNER TO postgres;

--
-- Name: inventory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.inventory_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventory_id_seq OWNER TO postgres;

--
-- Name: inventory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.inventory_id_seq OWNED BY public.inventory.id;


--
-- Name: locations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.locations (
    id integer NOT NULL,
    location_name text NOT NULL
);


ALTER TABLE public.locations OWNER TO postgres;

--
-- Name: locations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.locations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.locations_id_seq OWNER TO postgres;

--
-- Name: locations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.locations_id_seq OWNED BY public.locations.id;


--
-- Name: shopping_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shopping_list (
    id integer NOT NULL,
    food_id integer NOT NULL,
    num_units integer DEFAULT 1,
    date_added date NOT NULL
);


ALTER TABLE public.shopping_list OWNER TO postgres;

--
-- Name: shopping_list_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.shopping_list_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shopping_list_id_seq OWNER TO postgres;

--
-- Name: shopping_list_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.shopping_list_id_seq OWNED BY public.shopping_list.id;


--
-- Name: shopping_trip_items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shopping_trip_items (
    id integer NOT NULL,
    shopping_trip_id integer NOT NULL,
    food_id integer NOT NULL,
    price double precision DEFAULT 0.00 NOT NULL
);


ALTER TABLE public.shopping_trip_items OWNER TO postgres;

--
-- Name: shopping_trip_items_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.shopping_trip_items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shopping_trip_items_id_seq OWNER TO postgres;

--
-- Name: shopping_trip_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.shopping_trip_items_id_seq OWNED BY public.shopping_trip_items.id;


--
-- Name: shopping_trips; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shopping_trips (
    id integer NOT NULL,
    location_id integer NOT NULL,
    date date NOT NULL
);


ALTER TABLE public.shopping_trips OWNER TO postgres;

--
-- Name: shopping_trips_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.shopping_trips_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shopping_trips_id_seq OWNER TO postgres;

--
-- Name: shopping_trips_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.shopping_trips_id_seq OWNED BY public.shopping_trips.id;


--
-- Name: foods id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foods ALTER COLUMN id SET DEFAULT nextval('public.foods_id_seq'::regclass);


--
-- Name: inventory id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inventory ALTER COLUMN id SET DEFAULT nextval('public.inventory_id_seq'::regclass);


--
-- Name: locations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.locations ALTER COLUMN id SET DEFAULT nextval('public.locations_id_seq'::regclass);


--
-- Name: shopping_list id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shopping_list ALTER COLUMN id SET DEFAULT nextval('public.shopping_list_id_seq'::regclass);


--
-- Name: shopping_trip_items id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shopping_trip_items ALTER COLUMN id SET DEFAULT nextval('public.shopping_trip_items_id_seq'::regclass);


--
-- Name: shopping_trips id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shopping_trips ALTER COLUMN id SET DEFAULT nextval('public.shopping_trips_id_seq'::regclass);


--
-- Data for Name: foods; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.foods (id, name, auto_buy) FROM stdin;
1	Milk	t
2	Bread	t
3	Eggs	t
4	Broccoli	f
5	Strawberries	f
6	Bananas	t
7	Turkey meat	f
8	Chicken breast	f
\.


--
-- Data for Name: inventory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.inventory (id, food_id, shopping_trip_item_id, in_stock, expiration_date) FROM stdin;
1	7	1	t	2024-07-31
2	4	2	t	2024-07-21
3	5	3	f	2024-07-19
4	2	4	t	2024-07-31
\.


--
-- Data for Name: locations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.locations (id, location_name) FROM stdin;
1	Unknown
2	Walmart
3	Giant Eagle
4	Sams
5	Aldis
\.


--
-- Data for Name: shopping_list; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shopping_list (id, food_id, num_units, date_added) FROM stdin;
1	1	1	2024-07-18
2	3	1	2024-07-18
3	6	1	2024-07-18
\.


--
-- Data for Name: shopping_trip_items; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shopping_trip_items (id, shopping_trip_id, food_id, price) FROM stdin;
1	1	7	6.99
2	1	4	2.99
3	2	5	2.99
4	2	2	3.99
\.


--
-- Data for Name: shopping_trips; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shopping_trips (id, location_id, date) FROM stdin;
1	2	2024-07-17
2	4	2024-07-17
\.


--
-- Name: foods_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.foods_id_seq', 8, true);


--
-- Name: inventory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.inventory_id_seq', 4, true);


--
-- Name: locations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.locations_id_seq', 5, true);


--
-- Name: shopping_list_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.shopping_list_id_seq', 3, true);


--
-- Name: shopping_trip_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.shopping_trip_items_id_seq', 4, true);


--
-- Name: shopping_trips_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.shopping_trips_id_seq', 2, true);


--
-- Name: foods foods_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foods
    ADD CONSTRAINT foods_name_key UNIQUE (name);


--
-- Name: foods foods_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foods
    ADD CONSTRAINT foods_pkey PRIMARY KEY (id);


--
-- Name: inventory inventory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT inventory_pkey PRIMARY KEY (id);


--
-- Name: locations locations_location_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.locations
    ADD CONSTRAINT locations_location_name_key UNIQUE (location_name);


--
-- Name: locations locations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.locations
    ADD CONSTRAINT locations_pkey PRIMARY KEY (id);


--
-- Name: shopping_list shopping_list_food_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shopping_list
    ADD CONSTRAINT shopping_list_food_id_key UNIQUE (food_id);


--
-- Name: shopping_list shopping_list_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shopping_list
    ADD CONSTRAINT shopping_list_pkey PRIMARY KEY (id);


--
-- Name: shopping_trip_items shopping_trip_items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shopping_trip_items
    ADD CONSTRAINT shopping_trip_items_pkey PRIMARY KEY (id);


--
-- Name: shopping_trips shopping_trips_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shopping_trips
    ADD CONSTRAINT shopping_trips_pkey PRIMARY KEY (id);


--
-- Name: inventory fk_inventory_food; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT fk_inventory_food FOREIGN KEY (food_id) REFERENCES public.foods(id) ON DELETE CASCADE;


--
-- Name: inventory fk_inventory_shopping_trip_items; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT fk_inventory_shopping_trip_items FOREIGN KEY (shopping_trip_item_id) REFERENCES public.shopping_trip_items(id) ON DELETE SET NULL;


--
-- Name: shopping_list fk_shopping_list_food; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shopping_list
    ADD CONSTRAINT fk_shopping_list_food FOREIGN KEY (food_id) REFERENCES public.foods(id) ON DELETE CASCADE;


--
-- Name: shopping_trip_items fk_shopping_trip_items_food; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shopping_trip_items
    ADD CONSTRAINT fk_shopping_trip_items_food FOREIGN KEY (food_id) REFERENCES public.foods(id) ON DELETE CASCADE;


--
-- Name: shopping_trip_items fk_shopping_trip_items_shopping_trips; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shopping_trip_items
    ADD CONSTRAINT fk_shopping_trip_items_shopping_trips FOREIGN KEY (shopping_trip_id) REFERENCES public.shopping_trips(id) ON DELETE SET NULL;


--
-- Name: shopping_trips fk_shopping_trips_locations; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shopping_trips
    ADD CONSTRAINT fk_shopping_trips_locations FOREIGN KEY (location_id) REFERENCES public.locations(id) ON DELETE SET NULL;


--
-- PostgreSQL database dump complete
--

