FROM postgres:9.6.3  
ADD
https://github.com/faisalthaheem/hurtrade/releases/download/v1.0.0-alpha/db.init.sql
/docker-entrypoint-initdb.d/init.db.sql  
RUN chmod 555 /docker-entrypoint-initdb.d/init.db.sql  
  

