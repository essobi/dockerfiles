FROM particles/apache-php-proxy  
MAINTAINER Fabio Ferrari <fabio@particles.io>  
  
# Install required packages  
RUN apt-get update && apt-get install wget unzip gcc make dh-autoreconf
apache2-dev -y  
  
# Install IP2Location Apache Module  
RUN wget http://www.ip2location.com/downloads/ip2location-c-7.0.2.tar.gz && \  
tar xfvz ip2location-c-7.0.2.tar.gz && \  
wget http://www.ip2location.com/downloads/ip2location-apache-7.0.1.zip && \  
unzip ip2location-apache-7.0.1.zip  
  
WORKDIR ip2location-c-7.0.2  
RUN autoreconf -i -v --force && \  
./configure && \  
make && make install && make clean  
  
WORKDIR ../ip2location-apache-7.0.1  
RUN apxs2 -i -a -L /usr/local/lib -I ../ip2location-c-7.0.2/libIP2Location/
-lIP2Location -c mod_ip2location.c && \  
ldconfig && \  
a2enmod IP2Location  
  
WORKDIR ../  
RUN rm -f ip2location-c-7.0.2.tar.gz ip2location-apache-7.0.1.zip

