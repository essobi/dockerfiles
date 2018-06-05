FROM avatao/ubuntu:14.04  
  
ENV TERM dumb  
ENV NGINX_VERSION 1.8.1-1~trusty  
  
RUN apt-key adv \--keyserver hkp://pgp.mit.edu:80 \--recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -qy \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
gettext-base \  
php5-fpm \  
php5-sqlite \  
php5-mcrypt \  
php5-mysql \  
supervisor \  
apache2 \  
libapache2-mod-php5 \  
mariadb-server \  
php-apc \  
pwgen \  
&& rm -rf /var/lib/apt/lists/* /var/lib/mysql/* \  
&& php5enmod mcrypt  
  
COPY . /  
  
RUN mkdir -p /var/cache/apache2 /var/run/apache2 /var/lock/apache2
/var/log/apache2 /var/run/mysqld /var/log/mysql /var/run/php-fpm \  
&& chown -R user:user /var/cache/apache2 /var/run/apache2 /var/lock/apache2
/var/run/php-fpm \  
&& chown -R user:user /var/run/mysqld /var/log/mysql /var/lib/mysql \  
&& chown -R user:user /var/www /var/cache/nginx /var/log \  
&& mysql_install_db \--defaults-file=/etc/mysql/conf.d/my.cnf \  
&& chmod -R 765 /var/www \  
&& a2ensite site.conf \  
&& a2ensite codiad.conf \  
&& rm /etc/php5/fpm/pool.d/www.conf \  
&& rm /etc/nginx/conf.d/default.conf \  
&& mkdir /etc/nginx/sites-enabled \  
&& ln -s /etc/nginx/sites-available/codiad /etc/nginx/sites-enabled/codiad \  
&& ln -s /etc/nginx/sites-available/server /etc/nginx/sites-enabled/server \  
&& git clone https://github.com/Andr3as/Codiad-CompletePlus.git
/var/www/codiad/plugins/completeplus \  
&& cd /var/www \  
&& patch -p0 -f < /var/www/codiad.patch \  
&& cp -r /var/www/terminal /var/www/codiad/plugins/terminal \  
&& find /var/www/codiad -type f -exec chmod 664 {} +  
  
EXPOSE 8888  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

