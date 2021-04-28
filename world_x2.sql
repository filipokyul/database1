--
-- PostgreSQL database dump
--

-- Dumped from database version 12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)

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

--
-- Name: official; Type: TYPE; Schema: public; Owner: yulia1
--

CREATE TYPE public.official AS ENUM (
    'T',
    'F'
);


ALTER TYPE public.official OWNER TO yulia1;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: city; Type: TABLE; Schema: public; Owner: yulia1
--

CREATE TABLE public.city (
    id integer NOT NULL,
    name character(35) DEFAULT ''::bpchar NOT NULL,
    countrycode character(3) DEFAULT ''::bpchar NOT NULL,
    district character(20) DEFAULT ''::bpchar NOT NULL,
    info json
);


ALTER TABLE public.city OWNER TO yulia1;

--
-- Name: country; Type: TABLE; Schema: public; Owner: yulia1
--

CREATE TABLE public.country (
    code character(3) DEFAULT ''::bpchar NOT NULL,
    name character(52) DEFAULT ''::bpchar NOT NULL,
    capital integer,
    code2 character(2) DEFAULT ''::bpchar NOT NULL
);


ALTER TABLE public.country OWNER TO yulia1;

--
-- Name: countryinfo; Type: TABLE; Schema: public; Owner: yulia1
--

CREATE TABLE public.countryinfo (
    doc json,
    _id bytea NOT NULL,
    _json_schema json
);


ALTER TABLE public.countryinfo OWNER TO yulia1;

--
-- Name: countrylanguage; Type: TABLE; Schema: public; Owner: yulia1
--

CREATE TABLE public.countrylanguage (
    countrycode character(3) DEFAULT ''::bpchar NOT NULL,
    language character(30) DEFAULT ''::bpchar NOT NULL,
    isofficial public.official DEFAULT 'F'::public.official NOT NULL,
    percentage numeric(4,1) DEFAULT 0.0 NOT NULL
);


ALTER TABLE public.countrylanguage OWNER TO yulia1;

--
-- Name: first; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.first (
    id integer,
    name character(35)
);


ALTER TABLE public.first OWNER TO postgres;

--
-- Name: countryinfo countryinfo_pkey; Type: CONSTRAINT; Schema: public; Owner: yulia1
--

ALTER TABLE ONLY public.countryinfo
    ADD CONSTRAINT countryinfo_pkey PRIMARY KEY (_id);


--
-- Name: countrylanguage countrylanguage_pkey; Type: CONSTRAINT; Schema: public; Owner: yulia1
--

ALTER TABLE ONLY public.countrylanguage
    ADD CONSTRAINT countrylanguage_pkey PRIMARY KEY (countrycode, language);


--
-- PostgreSQL database dump complete
--

