FROM postgres:10.1  
ENV PG_MAX_WAL_SENDERS 8  
ENV PG_WAL_KEEP_SEGMENTS 8  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  

