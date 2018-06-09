FROM ubuntu:15.10  
MAINTAINER Olivier RICARD <olivier+genghis@talkspirit.com>  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL co.vidsy.build-date=$BUILD_DATE \  
co.vidsy.name="genghis" \  
co.vidsy.vcs-ref=$VCS_REF \  
co.vidsy.vcs-type="Git" \  
co.vidsy.vcs-url="https://github.com/talkspirit/genghis"  
  
#Setup container environment parameters  
ENV DEBIAN_FRONTEND noninteractive  
  
#Prepare the image  
RUN apt-get -y update  
  
#Install PHP packages  
RUN apt-get install -y -q php5-mongo libapache2-mod-php5  
  
RUN mkdir -p /var/www/genghis/  
  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
  
COPY conf /etc/apache2/sites-enabled/000-default.conf  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
RUN sed -i -e "s/Listen 80/Listen 8082/g" /etc/apache2/ports.conf  
  
# Enable apache mods.  
RUN a2enmod php5  
RUN a2enmod rewrite  
  
#Fetch from master.  
ADD https://raw.githubusercontent.com/bobthecow/genghis/develop/genghis.php
/var/www/genghis/  
  
RUN chown www-data.www-data /var/www/ -Rf  
  
EXPOSE 8082  
CMD ["apache2", "-D", "FOREGROUND"]  

