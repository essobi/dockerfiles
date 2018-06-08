FROM library/postgres:10  
ENV POSTGRES_USER docker  
ENV POSTGRES_PASSWORD docker  
ENV POSTGRES_DB MarketplaceCore  
  
ADD patches /docker-entrypoint-initdb.d/  
ADD patches/data_scripts /docker-entrypoint-initdb.d/  
  
VOLUME /etc/postgresql/data  
VOLUME /var/log/postgresql  
VOLUME /var/lib/postgresql/data  
  
EXPOSE 5432

