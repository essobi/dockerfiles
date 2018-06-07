FROM postgres:alpine  
MAINTAINER Scott Willson "<scott.willson@gmail.com>"  
COPY bin/create_databases /docker-entrypoint-initdb.d/create_databases.sh  
COPY bin/seed /docker-entrypoint-initdb.d/seed.sh  
COPY schema.sql /docker-entrypoint-initdb.d/schema  

