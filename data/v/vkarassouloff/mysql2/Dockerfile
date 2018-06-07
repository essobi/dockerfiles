FROM mysql:5.6  
  
ADD 1-SCHEMA.sql /docker-entrypoint-initdb.d/1.sql  
ADD 2-PRIVILEGES.sql /docker-entrypoint-initdb.d/2.sql  
ADD 3-ENTRIES.sql /docker-entrypoint-initdb.d/3.sql  

