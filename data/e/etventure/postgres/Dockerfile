FROM postgres:9.5  
MAINTAINER Alexander Pinnecke <alexander.pinnecke@googlemail.com>  
  
RUN mkdir -p /docker-entrypoint-initdb.d/  
ADD initdb/config.sh /docker-entrypoint-initdb.d/  
ADD initdb/init.sql /docker-entrypoint-initdb.d/  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  

