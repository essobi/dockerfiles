FROM postgres:9.3  
MAINTAINER Vitradisa Pratama (vitradisapratama@gmail.com)  
  
RUN apt-get update && apt-get install -y postgis-2.1 && rm -rf
/var/lib/apt/lists/*  
  
RUN echo "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology; CREATE
EXTENSION fuzzystrmatch; CREATE EXTENSION postgis_tiger_geocoder;" > docker-
entrypoint-initdb.d/enable_postgis.sql  
  
EXPOSE 5432

