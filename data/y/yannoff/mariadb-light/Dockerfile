FROM alpine:latest  
MAINTAINER Yannoff <https://github.com/yannoff>  
  
WORKDIR /var/lib/mysql  
VOLUME ["/var/lib/mysql"]  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
# No need to install mysql-client, as we only want the server here  
RUN apk add --update mysql && rm -f /var/cache/apk/*  
  
# Create daemon socket dir, as MySQL install doesn't take care of it  
RUN mkdir /run/mysqld  
  
EXPOSE 3306  
ENTRYPOINT ["/docker-entrypoint.sh"]  

