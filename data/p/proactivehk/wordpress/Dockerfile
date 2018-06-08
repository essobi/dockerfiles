FROM wordpress:4.9-php7.0  
MAINTAINER Jonathan Tse "jtse@proactivesystem.com.hk"  
RUN apt-get update && \  
apt-get install -y ssmtp && \  
apt-get clean  
  
ADD ssmtp.ini /usr/local/etc/php/conf.d/ssmtp.ini

