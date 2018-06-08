FROM debian:jessie  
RUN apt-get update && apt-get -y upgrade && apt-get -y install libapache2-mod-
php5 php5-mysql php5-gd php5-memcached php-pear && \  
a2enmod headers rewrite ssl && a2dismod status && \  
ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log && \  
rm -rf /var/lib/{apt,dpkg} var/cache/apt /usr/share/man /usr/share/doc  
EXPOSE 80 443  
ENTRYPOINT [ "/usr/sbin/apachectl","-D","FOREGROUND" ]  

