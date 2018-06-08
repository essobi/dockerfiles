FROM postgres:10.0  
MAINTAINER Guillaume Luchet <guillaume@geelweb.org>  
  
# Install PostGIS  
RUN apt-get update -y  
RUN apt-get install -y postgresql-10-postgis-2.4  
  
# Add the initialization script  
COPY init-postgis.sh /docker-entrypoint-initdb.d/  

