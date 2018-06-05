FROM postgres:9.3  
  
MAINTAINER Laurent Leseigneur <laurent.leseigneur@bonitasoft.com>  
COPY init-databases.sql /docker-entrypoint-initdb.d/init-databases.sql  
COPY set-max_prepared_transactions.sh /docker-entrypoint-initdb.d/set-
max_prepared_transactions.sh

