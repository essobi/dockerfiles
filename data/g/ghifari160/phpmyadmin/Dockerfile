FROM ghifari160/apache-php56:16.04  
MAINTAINER Ghifari160 <ghifari160@ghifari160.com>  
  
# Disable interactive functions  
ENV DEBIAN_FRONTEND noninteractive  
  
# Download phpMyAdmin  
RUN mkdir -p /tmp/g16 && \  
wget https://files.phpmyadmin.net/phpMyAdmin/4.7.9/phpMyAdmin-4.7.9-all-
languages.tar.gz -O /tmp/g16/phpmyadmin.tar.gz  
  
# Add init script  
RUN mkdir -p /etc/g16  
ADD init.sh /etc/g16/init.sh  
RUN chown root:root /etc/g16/init.sh && chmod 711 /etc/g16/init.sh  
  
VOLUME ["/var/www"]  
  
ENTRYPOINT ["/etc/g16/init.sh"]  

