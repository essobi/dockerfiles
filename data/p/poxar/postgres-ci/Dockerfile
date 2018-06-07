FROM postgres:9.5.7-alpine  
ADD non-durable.sh /docker-entrypoint-initdb.d/non-durable.sh  
RUN chmod 0755 /docker-entrypoint-initdb.d/non-durable.sh  

