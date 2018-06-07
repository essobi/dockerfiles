FROM postgres:9.6  
ENV POSTGIS_MAJOR="2.3"  
RUN apt-get clean && apt-get update \  
&& apt-get install -y --no-install-recommends \  
postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR \  
postgis-$POSTGIS_MAJOR \  
rsyslog \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GIS_USER="gis" GIS_DB="gis" GIS_PASSWORD=""  
ENV PG_HBA_CONF_FILE="/docker-entrypoint-initdb.d/pg_hba.conf"  
ENV POSTGRESQL_CONF_FILE="/docker-entrypoint-initdb.d/postgresql.conf"  
RUN mkdir -p /docker-entrypoint-initdb.d  
COPY ./*.sh /docker-entrypoint-initdb.d/  
COPY ./*.conf /docker-entrypoint-initdb.d/  

