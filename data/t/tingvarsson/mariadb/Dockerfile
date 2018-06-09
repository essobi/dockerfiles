# mariadb  
#  
# Version 1.0.0  
FROM alpine:3.4  
MAINTAINER Thomas Ingvarsson <ingvarsson.thomas@gmail.com>  
  
RUN apk add --no-cache mariadb  
  
VOLUME /var/lib/mysql  
  
EXPOSE 3306  
CMD ["mysqld"]

