FROM ubuntu:14.04  
MAINTAINER "Paolo Mainardi" <paolo@twinbit.it>  
  
# Install and configure apache2  
RUN apt-get update -y && \  
apt-get install -y apache2 bindfs && \  
rm -rf /var/lib/apt/lists/*  
  
# Configure apache2 modules  
RUN a2enmod rewrite proxy_fcgi  
  
# Apache startup script  
COPY scripts/apache-start.sh /opt/bin/apache-start.sh  
COPY conf/default-vhost /etc/apache2/sites-enabled/000-default.conf  
RUN chmod +x /opt/bin/apache-start.sh  
  
# PORTS  
EXPOSE 80  
# Create folders and expose data volume.  
RUN mkdir -p /data/var/www && chown -R www-data:www-data /data/var/www  
RUN mkdir -p /data/var/log/apache2 && mkdir -p /var/lock/apache2  
VOLUME /data  
  
WORKDIR /opt/bin  
ENTRYPOINT ["/opt/bin/apache-start.sh"]  

