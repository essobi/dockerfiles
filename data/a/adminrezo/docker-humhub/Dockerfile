# Humhub  
# Tested on Debian Wheezy  
#  
# VERSION 0.0.1  
#  
FROM adminrezo/docker-lamp  
MAINTAINER Nico Dewaele "nico@adminrezo.fr"  
ENV DEBIAN_FRONTEND noninteractive  
  
# Updates & packages install  
RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q &&
apt-get -y -q autoclean && apt-get -y -q autoremove)  
RUN mysqld_safe start  
RUN apt-get install -y -q php5-gd php5-curl php5-sqlite php5-ldap php-apc wget
unzip cron  
RUN wget https://github.com/humhub/humhub/archive/master.zip  
RUN unzip master.zip  
RUN mv humhub-master /var/www/humhub  
RUN chown www-data:www-data -R /var/www/  
  
# Config  
ADD default-ssl /etc/apache2/sites-available/default-ssl  
ADD pre-conf.sh /pre-conf.sh  
RUN chmod 750 /pre-conf.sh  
RUN (/bin/bash -c /pre-conf.sh)  
RUN service apache2 stop  
RUN a2enmod ssl  
RUN a2enmod rewrite  
RUN a2dissite default  
RUN a2ensite default-ssl  
  
# Start services  
ADD supervisor-humhub.conf /etc/supervisor/conf.d/supervisor-humhub.conf  
EXPOSE 80 443  
CMD ["supervisord", "-n"]  

