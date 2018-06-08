FROM ghifari160/apache-php56:16.04  
MAINTAINER Ghifari160 <ghifari160@ghifari160.com>  
  
# Disable interactive functions  
ENV DEBIAN_FRONTEND noninteractive  
  
# Download the latest version of Wordpress  
RUN mkdir -p /tmp/g16 && \  
wget https://wordpress.org/latest.tar.gz -O /tmp/g16/wp.tar.gz  
  
# Add init script  
RUN mkdir -p /etc/g16  
ADD init.sh /etc/g16/init.sh  
RUN chown root:root /etc/g16/init.sh && chmod 711 /etc/g16/init.sh  
  
VOLUME ["/var/www"]  
  
ENTRYPOINT ["/etc/g16/init.sh"]  

