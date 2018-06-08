FROM postgres:9.5  
MAINTAINER Matúš Demko <matus.demko@ui42.sk>  
  
ENV POSTGIS_MAJOR 2.2  
ENV POSTGIS_VERSION 2.2  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends --fix-missing \  
postgresql-9.5-postgis-2.2 \  
osm2pgsql \  
osmosis \  
postgresql-9.5-postgis-2.2-scripts  
  
RUN mkdir -p /docker-entrypoint-initdb.d  
COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/postgis.sh  
  
RUN mkdir -p /data/import  
  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
EXPOSE 5432  

