#  
# Bowhead Dockerfile.  
# use from the bowhead dir as  
# `docker built -t bowhead bowhead/  
# then `docker run bowhead` and read the output at the end.  
# using `docker ps` and `docker exec -it {id} /bin/bash` to connect  
#  
FROM ej52/alpine-nginx-php  
  
MAINTAINER joeldg@rxmg.com  
  
RUN apk add --update  
  
RUN apk add bzip2 curl vim wget git make gcc nasm git ack  
RUN apk add nfs-utils jq py-pip libmcrypt-dev gnupg  
RUN apk add curl make gcc nasm supervisor nfs-utils  
RUN apk add redis screen  
RUN apk add mariadb mariadb-client  
RUN apk add make automake autoconf unzip patch patchutils g++ openssl-dev  
  
RUN pecl channel-update pecl.php.net  
RUN pecl install trader  
  
RUN mkdir -p /var/www/html/  
  
#install phpUnit & composer and add a healthcheck we can use in AWS  
RUN \  
wget "https://phar.phpunit.de/phpunit.phar" && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
echo "<?php phpinfo() ?>" > /var/www/html/healthcheck.php  
  
ADD . /var/www  
WORKDIR /var/www  
  
COPY resources/etc/ /etc/  
COPY resources/config_bowhead.sh /var/www/config_bowhead.sh  
  
RUN chmod +x /var/www/config_bowhead.sh  
  
# if this container is used in AWS you will need these for ECS  
# you will also want the ports below  
RUN \  
pip install awscli && \  
aws configure set preview.efs true  
  
#RUN usermod -u 1000 www-data  
EXPOSE 8080  
EXPOSE 2049  
EXPOSE 20048  
#  
# supervisord with nodaemon=true  
# it sits and waits and keeps docker going.  
#  
CMD ["/var/www/config_bowhead.sh"]  

