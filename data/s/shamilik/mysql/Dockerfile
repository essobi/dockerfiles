# Build an image of latest MySQL 5.6  
FROM mysql:5.6  
MAINTAINER Shamil Yakupov <shamilik@yandex.ru>  
  
COPY config.cnf /etc/mysql/conf.d/  
  
RUN apt-get update && apt-get dist-upgrade -y  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

