FROM postgres:9.6.3  
  
WORKDIR /var/www/driver2  
  
RUN apt-get clean  
RUN apt-get update  
  
RUN apt-get install -y postgresql-9.6-postgis-2.4  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh", "postgres"]  
  
RUN apt-get autoremove && \  
apt-get clean

