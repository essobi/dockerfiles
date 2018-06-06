FROM mysql:5.6  
MAINTAINER Stefan Lehmann <stefan.lehmann@unic.com>  
  
## copy the init-db-script to the according directory  
## the script will then be picked up by the mysql entrypoint script  
COPY init-db-script.sql /docker-entrypoint-initdb.d/  
  
## copy additional database settings recommended by hybris  
COPY hybris.cnf /etc/mysql/conf.d/

