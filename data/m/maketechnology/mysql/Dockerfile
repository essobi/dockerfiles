FROM mysql:5.7  
  
ENV MYSQL_ROOT_PASSWORD=root  
  
COPY 1.sakila-schema.sql /docker-entrypoint-initdb.d  
COPY 2.sakila-data.sql /docker-entrypoint-initdb.d  

