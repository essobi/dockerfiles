FROM nginx  
  
RUN apt-get update && apt-get install -y --no-install-recommends wget  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
COPY getrelease.sh /getrelease.sh  
RUN chmod +x /docker-entrypoint.sh  
RUN chmod +x /getrelease.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

