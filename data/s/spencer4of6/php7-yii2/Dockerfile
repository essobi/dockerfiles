FROM silintl/php7  
MAINTAINER Spencer Salisbuy <spencer.salisbury@gmail.com>  
  
# Copy an Apache vhost file into sites-enabled.  
COPY vhost-config.conf /etc/apache2/sites-enabled/  
  
# Install MySQL  
RUN \  
apt-get update && \  
echo "mysql-server mysql-server/root_password password root" | debconf-set-
selections && \  
echo "mysql-server mysql-server/root_password_again password root" | debconf-
set-selections && \  
apt-get install -y mysql-server mysql-client && \  
apt-get autoclean && apt-get clean && apt-get autoremove  
  
EXPOSE 80  
RUN apache2ctl graceful

