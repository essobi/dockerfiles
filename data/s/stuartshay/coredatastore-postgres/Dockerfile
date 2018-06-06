FROM postgres:9.6  
MAINTAINER Stuart Shay  
RUN apt-get update -y && \  
apt-get install -y postgresql-contrib-9.6 postgresql-9.6-postgis-2.3-scripts
postgis && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /scripts  
COPY scripts /scripts  
RUN chmod +x /scripts/PGPlaceholder.sh && mkdir -p /data  
  
COPY data /data  
COPY docker-entrypoint-initdb.d /docker-entrypoint-initdb.d  
  
RUN echo "host all all 0.0.0.0/0 md5" >> /var/lib/postgresql/data/pg_hba.conf
&& \  
echo "listen_addresses='*'" >> /var/lib/postgresql/data/postgresql.conf  

