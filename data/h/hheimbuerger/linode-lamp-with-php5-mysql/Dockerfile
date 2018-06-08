FROM linode/lamp:latest  
  
# install missing php5-mysql package  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y \  
php5-mysql && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# fix permission for certain directories possibly mapped as volumes  
RUN mkdir /www  
RUN chown -R mysql:mysql /var/lib/mysql  
RUN chown -R www-data:www-data /www  
  
# run MySQL in the background and Apache in the foreground  
CMD service mysql start && apache2ctl -e DEBUG -DFOREGROUND  

