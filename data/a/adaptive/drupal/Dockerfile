##  
# Drupal/SSH with Nginx, PHP5 and SQLite  
##  
FROM ubuntu:12.04  
MAINTAINER Mike Douglas http://www.github.com/mike-douglas/  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
  
RUN apt-get update && apt-get upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y supervisor openssh-
server nginx php5-fpm php5-sqlite php5-gd drush  
RUN update-rc.d nginx disable  
RUN update-rc.d php5-fpm disable  
RUN update-rc.d supervisor disable  
RUN update-rc.d ssh disable  
  
EXPOSE 22 80  
RUN mkdir -p /var/run/sshd /srv/drupal/www /srv/drupal/config /srv/data
/srv/logs /tmp  
  
ADD site.conf /srv/drupal/config/site.conf  
ADD nginx.conf /nginx.conf  
ADD php-fpm.conf /php-fpm.conf  
ADD supervisord.conf /supervisord.conf  
  
RUN cd /tmp && drush dl drupal && mv /tmp/drupal*/* /srv/drupal/www/ && rm -rf
/tmp/*  
RUN chmod a+w /srv/drupal/www/sites/default && mkdir
/srv/drupal/www/sites/default/files  
RUN chown -R www-data:www-data /srv/drupal/www/  
RUN cp /srv/drupal/www/sites/default/default.settings.php
/srv/drupal/www/sites/default/settings.php  
RUN chmod a+w /srv/drupal/www/sites/default/settings.php  
RUN chown www-data:www-data /srv/data  
  
RUN echo "root:root" | chpasswd  
  
ENTRYPOINT [ "/usr/bin/supervisord", "-n", "-c", "/supervisord.conf", "-e",
"trace" ]  

