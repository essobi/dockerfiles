FROM postgres:9.4  
MAINTAINER Peter Korduan <peter.korduan@gdi-service.de>  
  
ENV POSTGIS_MAJOR 2.3  
ENV PG_ROUTING_MAJOR 2.0  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR \  
postgis \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /docker-entrypoint-initdb.d  
COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/postgis.sh  

