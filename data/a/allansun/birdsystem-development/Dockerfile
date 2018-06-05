FROM ubuntu:latest  
  
# This Dockerfile is intended for development purpose only  
# It uses root as apache user to prevent synced folder permission issue  
MAINTAINER Allan Sun <allan.sun@bricre.com>  
  
WORKDIR /home  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER root  
ENV APACHE_RUN_GROUP root  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_SERVERNAME localhost  
  
# Update apt-get to make sure we get latest repos  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install apache, PHP, and supplimentary programs. curl and lynx-cur are for
debugging the container.  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install locales apache2 php5
php5-cli php5-mcrypt libapache2-mod-php5 php5-mysql php5-gd php-pear php-apc
php5-curl curl lynx lynx-cur vim htop wget  
  
# Instal composer  
RUN curl -sS "https://getcomposer.org/installer" | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Ensure mod_rewrite is enabled  
RUN a2enmod rewrite  
  
# Configure timezone and locale  
RUN echo "Europe/London" > /etc/timezone; dpkg-reconfigure -f noninteractive
tzdata  
RUN export LANGUAGE=en_US.UTF-8; export LANG=en_US.UTF-8; export
LC_ALL=en_US.UTF-8; locale-gen en_US.UTF-8; DEBIAN_FRONTEND=noninteractive
dpkg-reconfigure locales  
  
# Instal Zend Framework  
RUN wget
https://packages.zendframework.com/releases/ZendFramework-1.12.3/ZendFramework-1.12.3.tar.gz  
RUN mkdir /home/ZendFramework1  
RUN tar -xzf ZendFramework-1.12.3.tar.gz -C /home/  
RUN rm -f ZendFramework-1.12.3.tar.gz  
RUN pear install Image_Text-beta  
  
# php.ini settings  
RUN sed -ie 's/\;date\\.timezone\ \=/date\\.timezone\ \=\ Europe\/London/g'
/etc/php5/apache2/php.ini  
RUN sed -i "s/;include_path = \"\\.:.*/include_path =
\".:\/usr\/share\/php:\/home\/ZendFramework-1.12.3\/library\"/"
/etc/php5/apache2/php.ini  
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ALL \& ~E_NOTICE \&
~E_STRICT \& ~E_DEPRECATED/" /etc/php5/apache2/php.ini  
  
EXPOSE 80  
WORKDIR /www

