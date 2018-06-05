  
FROM ubuntu:12.04  
LABEL maintainer="tdmalone@gmail.com"  
  
RUN apt-get update && \  
apt-get install --assume-yes --no-install-recommends \  
apache2=2.2.22-1ubuntu1.11 \  
php5=5.3.10-1ubuntu3.26 \  
php5-cli=5.3.10-1ubuntu3.26 \  
libapache2-mod-php5=5.3.10-1ubuntu3.26 \  
php5-gd=5.3.10-1ubuntu3.26 \  
php5-mysql=5.3.10-1ubuntu3.26 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY vhost.conf /etc/apache2/sites-available/default  
COPY run.sh /usr/local/bin/run  
  
RUN chmod +x /usr/local/bin/run && \  
a2enmod rewrite  
  
EXPOSE 80  
VOLUME ["/var/www"]  
CMD ["/usr/local/bin/run"]  

