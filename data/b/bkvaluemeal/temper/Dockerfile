FROM debian:latest  
MAINTAINER bkvaluemeal <sirJustin.Willis@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y \  
supervisor \  
curl \  
nginx \  
mysql-server \  
php5-fpm \  
php5-mysql \  
&& curl --location https://www.phpmyadmin.net/downloads/phpMyAdmin-latest-all-
languages.tar.gz | tar xzf - \  
&& mv phpMyAdmin* phpmyadmin \  
&& cp phpmyadmin/config.sample.inc.php phpmyadmin/config.inc.php \  
&& echo "" >> phpmyadmin/config.inc.php \  
&& echo "\$cfg['Servers'][\$i]['AllowNoPassword'] = true;" >>
phpmyadmin/config.inc.php \  
&& echo "\$cfg['blowfish_secret'] = '$(date +%s | sha256sum | base64 | head -c
32 ; echo)';" >> phpmyadmin/config.inc.php \  
&& chown -R root:root phpmyadmin \  
&& mv phpmyadmin /var/www \  
&& mv /var/www/html/index* /var/www/html/index.html  
  
COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY conf/nginx.conf /etc/nginx/sites-available/default  
COPY res/phpmyadmin.sql /tmp/phpmyadmin.sql  
  
RUN mysqld_safe & \  
while ! mysqladmin ping --silent; do sleep 1; done \  
&& mysql -u root -e 'CREATE DATABASE phpmyadmin;' \  
&& mysql -u root phpmyadmin < /tmp/phpmyadmin.sql \  
&& rm /tmp/phpmyadmin.sql  
  
EXPOSE 80 443 3306 8080  
CMD ["/usr/bin/supervisord"]  

