FROM nextcloud:apache  
  
RUN apt-get update && \  
apt-get -y install libsmbclient-dev && \  
apt-get clean && \  
pecl install smbclient  
  
RUN echo 'extension=smbclient.so' > /usr/local/etc/php/conf.d/docker-php-
smbclient.ini  

