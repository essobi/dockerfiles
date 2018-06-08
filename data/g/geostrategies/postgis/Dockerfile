FROM mdillon/postgis:9.6  
RUN apt-get update && apt-get install -y postgresql-9.6-plv8
postgresql-9.6-pgrouting  
COPY plv8/ /plv8  
COPY pgbouncer/ /pgbouncer  
COPY initdb-postgis.sh /docker-entrypoint-initdb.d/postgis.sh

