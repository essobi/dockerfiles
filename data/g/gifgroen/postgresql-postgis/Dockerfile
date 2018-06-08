FROM postgres:9.4  
MAINTAINER Karsten Westra <karstenwestra@gmail.com>  
  
# Add the 'host all all 0.0.0.0/0 md5' to pg_hba.conf  
COPY options/auth_all.sh /docker-entrypoint-initdb.d/auth_all.sh  
  
# install postgis through apt  
RUN apt-get update  
RUN apt-get install -y postgresql-contrib \  
postgis \  
postgresql-9.4-postgis-2.1  
  

