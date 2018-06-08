FROM gliderlabs/logspout:master  
  
# Use custom entrypoint shell script  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

