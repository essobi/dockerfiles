FROM alpine:latest  
MAINTAINER Goeran Poehner "goeran.poehner@gmail.com"  
LABEL Description="Alpine based MariaDB image"  
  
WORKDIR /  
RUN apk update && apk upgrade && apk add mariadb mariadb-client  
COPY scripts/start.sh /usr/local/bin  
  
EXPOSE 3306  
VOLUME /var/lib/mysql  
  
ENTRYPOINT ["/usr/local/bin/start.sh"]  

