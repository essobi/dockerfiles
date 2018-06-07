FROM postgres:9.6  
MAINTAINER paul.trippett@tuskerdirect.com  
  
COPY files/postgres-docker-entrypoint.sh /docker-entrypoint.sh  
  
EXPOSE 5432  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["postgres"]  

