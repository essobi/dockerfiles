FROM postgres:9.4  
MAINTAINER Nuxeo <contact@nuxeo.com>  
  
RUN mkdir -p /docker-entrypoint-initdb.d/  
ADD initdb/config.sh /docker-entrypoint-initdb.d/  
ADD initdb/init.sql /docker-entrypoint-initdb.d/  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  

