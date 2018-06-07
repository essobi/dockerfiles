FROM avatao/ubuntu:14.04  
# Install common packages  
RUN apt-get -qy update \  
&& apt-get -qy install \  
apache2 \  
libapache2-mod-php5 \  
mariadb-server \  
php-apc \  
php5-fpm \  
php5-mcrypt \  
php5-mysql \  
pwgen \  
supervisor \  
&& rm -rf /var/lib/apt/lists/* /var/lib/mysql/*  
  
COPY . /  
  
# Initialize Apache2 and MySQL/MariaDB  
# TODO: Log to stdout so supervisord can forward it...  
RUN mkdir -p /var/cache/apache2 /var/run/apache2 /var/lock/apache2
/var/log/apache2 \  
&& chown -R user:user /var/cache/apache2 /var/run/apache2 /var/lock/apache2
/var/log /var/www \  
&& mkdir -p /var/run/mysqld /var/log/mysql \  
&& mysql_install_db --defaults-file=/etc/mysql/conf.d/my.cnf \  
&& chown -R user:user /var/run/mysqld /var/lib/mysql  
  
VOLUME ["/var/lib/mysql", "/var/run/mysqld", "/var/log/mysql"]  
  
VOLUME ["/var/cache/apache2", "/var/run/apache2", "/var/lock/apache2",
"/var/log/apache2"]  
  
USER user  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

