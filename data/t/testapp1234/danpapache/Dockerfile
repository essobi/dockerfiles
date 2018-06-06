<<<<<<< HEAD  
FROM ubuntu:16.04  
MAINTAINER Fer Uria <fauria@gmail.com>  
LABEL Description="Cutting-edge LAMP stack, based on Ubuntu 16.04 LTS.
Includes .htaccess support and popular PHP7 features, including composer and
mail() function." \  
License="Apache License 2.0" \  
Usage="docker run -d -p [HOST WWW PORT NUMBER]:80 -p [HOST DB PORT
NUMBER]:3306 -v [HOST WWW DOCUMENT ROOT]:/var/www/html -v [HOST DB DOCUMENT
ROOT]:/var/lib/mysql fauria/lamp" \  
Version="1.0"  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
COPY debconf.selections /tmp/  
RUN debconf-set-selections /tmp/debconf.selections  
=======  
#This is the file from which image is built. We need to create image using
command docker build -t <path/to/Dockerfile>  
#FROM ubuntu:latest  
FROM ubuntu:latest  
MAINTAINER Dan Pupius <dan@pupi.us>  
  
# Install apache, PHP, and supplimentary programs. openssh-server, curl, and
lynx-cur are for debugging the container.  
RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive
apt-get -y install \  
apache2 php7.0 php7.0-mysql libapache2-mod-php7.0 lynx-cur mysql  
RUN apt-get -y install \  
elinks elinks-data elinks-doc nano git  
  
# Enable apache mods.  
RUN a2enmod php7.0  
RUN a2enmod rewrite  
RUN mkdir -p /app  
>>>>>>> 37b5c20816d959a27ddeb0ceee8c53e55e8183f4  
  
RUN apt-get install -y zip unzip  
RUN apt-get install -y \  
php7.0 \  
php7.0-bz2 \  
php7.0-cgi \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-dev \  
php7.0-enchant \  
php7.0-fpm \  
php7.0-gd \  
php7.0-gmp \  
php7.0-imap \  
php7.0-interbase \  
php7.0-intl \  
php7.0-json \  
php7.0-ldap \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-odbc \  
php7.0-opcache \  
php7.0-pgsql \  
php7.0-phpdbg \  
php7.0-pspell \  
php7.0-readline \  
php7.0-recode \  
php7.0-snmp \  
php7.0-sqlite3 \  
php7.0-sybase \  
php7.0-tidy \  
php7.0-xmlrpc \  
php7.0-xsl \  
php7.0-zip  
RUN apt-get install apache2 libapache2-mod-php7.0 -y  
RUN apt-get install mariadb-common mariadb-server mariadb-client -y  
RUN apt-get install postfix -y  
RUN apt-get install git nodejs composer nano tree vim curl ftp -y  
#RUN npm install -g bower grunt-cli gulp  
ENV LOG_STDOUT **Boolean**  
ENV LOG_STDERR **Boolean**  
ENV LOG_LEVEL warn  
ENV ALLOW_OVERRIDE All  
ENV DATE_TIMEZONE UTC  
ENV TERM dumb  
  
COPY index.php /var/www/html/  
COPY run-lamp.sh /usr/sbin/  
  
RUN a2enmod rewrite  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN chmod +x /usr/sbin/run-lamp.sh  
RUN chown -R www-data:www-data /var/www/html  
  
VOLUME /var/www/html  
VOLUME /var/log/httpd  
VOLUME /var/lib/mysql  
VOLUME /var/log/mysql  
  
EXPOSE 80  
EXPOSE 3306  
  
<<<<<<< HEAD  
CMD ["/usr/sbin/run-lamp.sh"]  
=======  
# By default start up apache in the foreground, override with /bin/bash for
interative.  
CMD /usr/sbin/apache2ctl -D FOREGROUND  
#CMD ["exec","run-lamp.sh"]  
>>>>>>> 37b5c20816d959a27ddeb0ceee8c53e55e8183f4  

