FROM postgres:9.3.5  
COPY tsearch_data /usr/share/postgresql/$PG_MAJOR/tsearch_data  
  
COPY docker-entrypoint.sh /  
  
RUN chmod +x /docker-entrypoint.sh  

