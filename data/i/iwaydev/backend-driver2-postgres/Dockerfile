FROM postgres:9.6.3  
WORKDIR /var/www/driver2  
  
RUN apt-get update  
  
RUN apt-get install -y postgresql-9.1-postgis  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh", "postgres"]  
ENTRYPOINT ["psql", "-U postgres", "-c 'CREATE EXTENSION postgis'"]  
ENTRYPOINT ["psql", "-U postgres", "-c 'CREATE EXTENSION btree_gist'"]  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh", "postgres"]  
  
# CREATE INDEX geozones_test_location_idx ON geozones_test USING
GIST(location);  
RUN apt-get autoremove && \  
apt-get clean  

