FROM phusion/baseimage:0.9.19  
# Basic install of apache  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
apache2 \  
&& \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add custom apache configuration and prepare services.  
COPY files/etc/ /etc/  
# Switch docroot from html to web to be docker-compose compatible  
RUN \  
mv /var/www/html /var/www/web  
  
# Enable needed apache modules and configuration added above  
RUN \  
a2enmod rewrite && \  
a2enmod proxy_fcgi && \  
a2enmod remoteip && \  
a2enmod expires && \  
a2enconf allow-override-all && \  
a2enconf php-fpm  
  
EXPOSE 80  

