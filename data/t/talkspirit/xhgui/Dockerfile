FROM ubuntu:15.10  
MAINTAINER Olivier RICARD <olivier+xhui@talkspirit.com>  
  
#Setup container environment parameters  
ENV DEBIAN_FRONTEND noninteractive  
  
#Prepare the image  
RUN apt-get -y update  
  
#Install PHP packages  
RUN apt-get install -y -q php5-mongo php5-mcrypt libapache2-mod-php5 git  
  
RUN cd /etc/php5/cli/conf.d;ln -s ../../mods-available/mcrypt.ini
20-mcrypt.ini  
  
RUN mkdir -p /var/www/  
WORKDIR /var/www/  
RUN git clone https://github.com/perftools/xhgui.git  
RUN cd xhgui && php install.php  
  
COPY conf.default.php /var/www//xhgui/config/config.php  
  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
COPY apache.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
RUN sed -i -e "s/Listen 80/Listen 8083/g" /etc/apache2/ports.conf  
  
# Enable apache mods.  
RUN a2enmod php5  
RUN a2enmod rewrite  
  
RUN chown www-data.www-data /var/www/ -Rf  
  
EXPOSE 8083  
CMD ["apache2", "-D", "FOREGROUND"]  

