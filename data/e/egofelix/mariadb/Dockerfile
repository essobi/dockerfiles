FROM alpine  
  
MAINTAINER EgoFelix <docker@egofelix.de>  
  
# Install mariadb  
RUN apk --no-cache add \  
mariadb  
  
COPY run.sh /run.sh  
RUN chmod 755 /run.sh  
  
EXPOSE 3306  
VOLUME ["/var/lib/mysql"]  
ENTRYPOINT ["/run.sh"]

