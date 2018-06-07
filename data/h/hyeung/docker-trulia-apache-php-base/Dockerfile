# FE apache php base container  
# base off of ubuntu for now  
FROM ubuntu  
  
MAINTAINER Hinling Yeung  
  
# Make DEBIAN_FRONTEND less chatty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update the default application repository sources list  
RUN apt-get update  
  
# Install apache 2  
RUN apt-get -y install apache2  
  
# Install php5  
RUN apt-get -y install php5 libapache2-mod-php5 php5-dev  
  
# Install xdebug  
RUN apt-get -y install php5-xdebug  
  
# Install mysql client  
RUN apt-get -y install libapache2-mod-auth-mysql php5-mysql mysql-client  
  
# Install PEAR  
RUN apt-get -y install php-pear  
  
# Install phpmods  
RUN pear upgrade --force pear  
RUN printf "no\n" | pecl install stomp-1.0.5  
RUN apt-get -y install libpcre3-dev  
RUN apt-get -y install pkg-config  
# RUN pecl install APC -- no APC for php5.5  
RUN pecl install xdebug  
  
# Install apache libs  
RUN apt-get -y install apache2-dev apache2-doc  
  
# Install all the php libraries  
RUN apt-get -y install php5-common libapache2-mod-php5 php5-cli  
RUN apt-get -y install php5-gd  
RUN apt-get -y install php5-mcrypt  
RUN apt-get -y install php5-curl  
RUN apt-get -y install libmemcached-dev  
RUN apt-get -y install php5-memcached  
RUN apt-get -y install imagemagick --fix-missing  
RUN apt-get -y install mcrypt php5-mcrypt  
RUN php5enmod mcrypt  
RUN apt-get -y install php5-xsl  
  
# helper tools  
RUN apt-get -y install telnet  
RUN apt-get -y install wget  
  
# configure apache  
RUN a2enmod rewrite  
ADD apache_conf/apache2.conf /etc/apache2/apache2.conf  
ADD apache_conf/000-default.conf /etc/apache2/sites-enabled/000-default.conf  
ADD apache_conf/php.ini /etc/php5/apache2/php.ini  
ADD apache_conf/mysql_password.so /usr/lib/php5/20121212/mysql_password.so  
ADD apache_conf/20-xdebug.ini /etc/php5/cli/conf.d/20-xdebug.ini  
  
# Install Opcache and APCu  
ADD apache_conf/install_opcache_apcu.sh .  
RUN ./install_opcache_apcu.sh  
  
# Install Couchbase  
ADD apache_conf/install_couchbase.sh .  
RUN ./install_couchbase.sh  
  
# Install igbinary  
ADD apache_conf/install_igbinary.sh .  
RUN ./install_igbinary.sh  
  
# Install stomp  
ADD apache_conf/install_stomp.sh .  
RUN ./install_stomp.sh  
  
# Create smarty dir  
RUN mkdir -p /data/smarty  
RUN chgrp -R www-data /data/smarty  
RUN chmod -R 770 /data/smarty  
  
# Grant permisson for writing session info  
RUN chgrp -R www-data /var/lib/php5  
RUN chmod -R 770 /var/lib/php5  
  
ENV DEBIAN_FRONTEND newt  
ENTRYPOINT ["/usr/sbin/apachectl", "-DFOREGROUND"]  

