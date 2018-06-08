FROM ubuntu:xenial  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install \  
php7.0 \  
php7.0-cgi \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-dev \  
php7.0-gd \  
php7.0-gmp \  
php7.0-json \  
php7.0-ldap \  
php7.0-mysql \  
php7.0-odbc \  
php7.0-opcache \  
php7.0-pspell \  
php7.0-readline \  
php7.0-sqlite3 \  
php7.0-tidy \  
php7.0-xmlrpc \  
php7.0-xsl \  
php7.0-fpm \  
php7.0-intl \  
php7.0-mcrypt && apt-get clean  
  
# Configure  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
CMD ["/bin/bash", "/start.sh"]  

