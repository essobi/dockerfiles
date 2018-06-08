FROM mysql:5.7  
  
COPY my.cnf /etc/mysql/conf.d/  
COPY create-eventstore-schema.sql /docker-entrypoint-initdb.d/  

