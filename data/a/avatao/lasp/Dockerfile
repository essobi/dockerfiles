FROM avatao/ubuntu:16.04  
# Install common packages  
RUN apt-get -qy update  
RUN apt-get -qy install \  
apache2 \  
php7.0-sqlite3 \  
sqlite3 \  
php \  
libapache2-mod-php \  
supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN rm -fr /var/www/html  
  
COPY . /  
  
RUN mkdir -p /var/cache/apache2 /var/run/apache2 /var/lock/apache2
/var/log/apache2 \  
&& chown -R user:user /var/cache/apache2 /var/run/apache2 /var/lock/apache2
/var/log /var/www \  
&& cd /db \  
&& cat database.sql | sqlite3 database.sqlite3 \  
&& a2enmod rewrite  
  
#VOLUME ["/db"]  
VOLUME ["/var/cache/apache2", "/var/run/apache2", "/var/lock/apache2",
"/var/log/apache2"]  
  
EXPOSE 8888  
USER user  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

