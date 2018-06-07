FROM mysql:5.7  
MAINTAINER Shane Genschaw  
  
COPY docker-entrypoint-initdb.d /docker-entrypoint-initdb.d  
COPY initdb /initdb  
RUN cat /initdb/test_db/employees.sql \  
/initdb/test_db/objects.sql \  
/initdb/users.sql > /initdb/test_db/initdb.sql  

