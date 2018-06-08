FROM postgres:9.5  
MAINTAINER paul@trippett.org  
  
COPY docker-entrypoint.sh /  
  
EXPOSE 5432  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["postgres"]  

