FROM php:fpm  
MAINTAINER Mark Hummel <mdh@raquette.com>  
  
#ENV DEBIAN_FRONTEND noninteractive  
#ENV MYSQL_HOST 127.0.0.1  
#ENV MYSQL_PORT 3306  
#ENV MYSQL_USER root  
#ENV RESTORE_DB_CHARSET utf8  
#ENV RESTORE_DB_COLLATION utf8_bin  
#ENV S3_PATH mysql  
#ENV WAIT_FOR_SERVER yes  
#  
RUN apt-get update \  
# && apt-get install -yq git nginx php5-fpm php5-cli php5-curl curl \  
&& apt-get install -yq git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
RUN mkdir /var/log/dyndns \  
&& touch /var/log/dyndns/DigitalOcean.DynDns.log \  
&& chown -R www-data:www-data /var/log/dyndns \  
&& chmod -R 770 /var/log/dyndns \  
&& mkdir /install \  
&& cd /install \  
&& git clone https://github.com/digitalm3/DigitalOcean_dyndns nic \  
&& cd nic && curl -sS https://getcomposer.org/installer | php \  
&& php composer.phar install  
  
#ADD startup.sh /startup.sh  
#ADD default /etc/nginx/sites-enabled/default  
#RUN rm -rf /usr/share/nginx/html/nic/digitalocean.config.php  
#VOLUME /usr/share/nginx/html/nic/digitalocean.config.php  
#EXPOSE 80  
#CMD [ "/bin/bash", "/startup.sh" ]  

