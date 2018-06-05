FROM postgres:9.6  
MAINTAINER Camptocamp "info@camptocamp.com"  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y postgresql-9.6-postgis-2.3
postgresql-9.6-postgis-2.3-scripts \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY 00-postgis.sql /docker-entrypoint-initdb.d/  

