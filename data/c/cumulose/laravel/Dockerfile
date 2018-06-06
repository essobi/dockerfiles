FROM ubuntu:16.04  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN export LANG=C.UTF-8 && \  
apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:ondrej/php && \  
apt-get update  
  
RUN apt-get install -y apache2 \  
php7.1 \  
php7.1-curl \  
php7.1-mysql \  
php7.1-mcrypt \  
php7.1-mbstring \  
php7.1-xml \  
php7.1-sqlite3 \  
php7.1-gd \  
php7.1-ldap \  
php7.1-gmp \  
libapache2-mod-php7.1 \  
phpunit \  
unzip  
  
#Make sure to set CLI PHP to run at 7.1 since 7.2 is getting deployed for some
reason  
RUN update-alternatives --set php /usr/bin/php7.1  
  
RUN a2enmod rewrite && \  
a2enmod ssl  

