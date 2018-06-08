FROM postgres:9.3.10  
MAINTAINER Jakob Runge <runjak@gmail.com>  
  
LABEL lingdb="postgres" \  
version="1.0.1" \  
documentation="https://github.com/lingdb/container/wiki/postgres"  
  
COPY setup.sql /docker-entrypoint-initdb.d  

