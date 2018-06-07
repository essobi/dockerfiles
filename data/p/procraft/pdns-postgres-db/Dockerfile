FROM postgres:10-alpine  
  
LABEL maintainer="Procraft Team"  
  
COPY init-user-db.sh /docker-entrypoint-initdb.d/  
COPY schema.sql /tmp/  
  
ENV PDNS_DB_NAME=pdns \  
PDNS_DB_USER=pdns \  
PDNS_DB_PASSWORD=changeme  

