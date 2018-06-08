FROM debian:wheezy  
MAINTAINER Potens  
LABEL Description="Cutting-edge LAMP stack, based on Ubuntu 16.04 LTS.
Includes .htaccess support and popular PHP5 features, including composer and
mail() function." \  
License="Apache License 2.0" \  
Usage="docker run -d -p 80:80 -p 3306:3306 -p 4242:22 -p 27017:27017 lamp" \  
Version="0.2"  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
#APACHE2  
RUN apt-get install -y \  
php5 \  
php5-cgi \  
php5-cli \  
php5-common \  
php5-curl \  
php5-dev \  
php5-enchant \  
php5-fpm \  
php5-gd \  
php5-gmp \  
php5-imap \  
php5-interbase \  
php5-intl \  
php5-json \  
php5-ldap \  
php5-mcrypt \  
php5-mysql \  
php5-odbc \  
php5-pgsql \  
php5-pspell \  
php5-recode \  
php5-snmp \  
php5-sybase \  
php5-tidy \  
php5-xmlrpc \  
php5-xsl \  
php-pear  
  
RUN apt-get install libcurl3-openssl-dev -y  
RUN apt-get install apache2 libapache2-mod-php5 -y  
  
#PHP - mongo  
RUN apt-get install -y autoconf g++ make libcurl4-openssl-dev openssl pkg-
config libsasl2-dev libpcre3-dev libssl-dev curl build-essential git nano  
RUN pecl install mongodb  
RUN echo "extension=mongodb.so" >> /etc/php5/apache2/php.ini  
  
#Node  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install pm2 -g  
  
#SSH  
RUN apt-get install openssh-server -y  
COPY static_files/sshd_config /etc/ssh/sshd_config  
  
EXPOSE 80  
EXPOSE 3306  
EXPOSE 4242  
EXPOSE 27017  
RUN service apache2 start  
RUN service php5-fpm start  
RUN service ssh start  
  
CMD tail -f /dev/null

