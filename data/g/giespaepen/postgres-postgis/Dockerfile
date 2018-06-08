FROM postgres:9.6  
LABEL maintainer="gie.spaepen@rombit.be"  
  
RUN apt-get update && \  
apt-get -y install wget && \  
sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt xenial-pgdg main" >>
/etc/apt/sources.list' && \  
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-
key add - && \  
apt-get update && \  
apt-get -y install postgresql-9.6-postgis-2.3 postgresql-contrib-9.6
postgresql-9.6-postgis-scripts && \  
apt-get -y install postgis && \  
apt-get -y install postgresql-9.6-pgrouting && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get purge -y --auto-remove  
  
COPY docker-startup.sh /usr/local/bin/  
RUN chmod 755 /usr/local/bin/docker-startup.sh  
ENTRYPOINT ["docker-startup.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]

