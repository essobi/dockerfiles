FROM postgres:9.5  
MAINTAINER Kamil Cholewiński <kamil.cholewinski@unit9.com>  
  
RUN apt-get update && \  
apt-get install --yes --no-install-recommends \  
postgresql-9.5-postgis-2.4 \  
postgresql-9.5-postgis-2.4-scripts \  
&& rm -rf /var/cache/apt /var/lib/apt/lists  
  
COPY postgres.sh /postgres.sh  
RUN chmod +x /postgres.sh && \  
chmod +x /docker-entrypoint.sh  
  
VOLUME ["/var/lib/postgresql/data", "/etc/postgres-credentials"]  
  
CMD ["/postgres.sh"]  

