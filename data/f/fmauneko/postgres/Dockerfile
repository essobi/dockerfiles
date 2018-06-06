FROM postgres:10-alpine  
  
RUN mkdir -p /docker-entrypoint-initdb.d  
COPY ./create_extensions.sh /docker-entrypoint-initdb.d/create_extensions.sh  

