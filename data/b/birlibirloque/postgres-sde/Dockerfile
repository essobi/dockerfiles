FROM postgres:9.6.3  
  
ENV POSTGRES_DATA /var/lib/postgresql/data  
RUN usermod -u 1000 postgres && groupmod -g 1000 postgres && chown -R
postgres:postgres ${POSTGRES_DATA}  
VOLUME ${POSTGRES_DATA}  
EXPOSE 5432  

