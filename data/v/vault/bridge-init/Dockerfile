FROM debian  
  
RUN apt-get update && apt-get install -y wget mysql-client --no-install-
recommends && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

