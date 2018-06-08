FROM ubuntu:17.10  
ENV DEBIAN_FRONTEND=noninteractive  
  
MAINTAINER Marcos Freitas <marcosfreitas@c4network.com.br>  
  
# clean and update sources  
RUN apt-get clean && apt-get update  
  
# install lo locales support  
RUN apt-get install locales  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# instalations  
RUN apt-get update && apt-get install -y software-properties-common nano exif  
  
RUN add-apt-repository ppa:ondrej/php  
  
RUN apt-get update && apt-get install -y libbz2-dev libfreetype6-dev libjpeg-
dev libtiff-dev libgd-dev libmcrypt-dev libpng-dev libxml2-dev zlib1g-dev \  
php7.1 \  
libapache2-mod-php7.1 php7.1-fpm php7.1-dev php7.1-cli php7.1-common
php7.1-intl php7.1-bcmath php7.1-mbstring php7.1-soap php7.1-xml \  
php7.1-zip php7.1-apcu php7.1-json php7.1-gd php7.1-curl php7.1-mcrypt
php7.1-mysql php7.1-sqlite php-memcached php7.1-mbstring \  
php7.1-mcrypt php7.1-soap php7.1-opcache  
# mysql-client mysql-server  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
COPY config/php.ini /usr/local/etc/php/  
  
# Update the default apache site with the config we created.  
ADD config/apache2.conf /etc/apache2/sites-enabled/000-default.conf  
  
RUN a2enmod headers  
RUN a2enmod rewrite  
#CMD ["/usr/sbin/apache2ctl","restart  
# make the src a volume  
#VOLUME ["www/:/var/www/html/"]  
RUN chown -R www-data:www-data /var/www/html  
  
EXPOSE 80  
#ENTRYPOINT ["/usr/sbin/apache2ctl","-DFOREGROUND"]  
CMD ["/bin/bash"]  

