# FROM ubuntu:16.04  
  
# ENV DEBIAN_FRONTEND noninteractive  
  
# RUN apt-get update && \  
# apt-get dist-upgrade -y && \  
# apt-get install -y \  
# apache2 \  
# php \  
# php-cli \  
# php-fpm \  
# php-gd \  
# php-ssh2 \  
# libapache2-mod-php \  
# php-mcrypt \  
# mysql-server \  
# php-mysql \  
# git \  
# php-curl \  
# php-json \  
# phpmyadmin \  
# socat  
  
  
  
# # COPY apache_default /etc/apache2/sites-available/000-apache_default.conf  
# # COPY run /usr/local/bin/run  
  
# RUN chown -R root:www-data /var/www  
# RUN chmod u+rwx,g+rx,o+rx /var/www  
# RUN find /var/www -type d -exec chmod u+rwx,g+rx,o+rx {} +  
# RUN find /var/www -type f -exec chmod u+rw,g+rw,o+r {} +  
  
# RUN a2enmod rewrite  
# # 호스트의 저장소와 연결할 수 있는 볼륨을 정의합니다.  
# # VOLUME /var/www/html  
# # WORKDIR /var/www/html  
  
# ENV APACHE_RUN_USER www-data  
# ENV APACHE_RUN_GROUP www-data  
# ENV APACHE_LOG_DIR /var/log/apache2  
  
  
  
# # 실행 커맨드  
# EXPOSE 80 3306  
# CMD sudo service apache2 start  
  
  
FROM 1and1internet/ubuntu-16-apache-php-7.1  
MAINTAINER kimps@mshuttle.co.kr  
ARG DEBIAN_FRONTEND=noninteractive  
  
  
  
  
  
# docker service create \  
# \--name mbackend \  
# \--replicas 3 \  
# \--mount type=volume,source=my-volume,destination=/var/www/html,volume-
label="color=red",volume-label="shape=round" \  
# fart86/php-server  

