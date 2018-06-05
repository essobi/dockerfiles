FROM ubuntu:trusty  
MAINTAINER romracer <romracer@gmail.com>  
  
ENV PDNSCONF_LAUNCH="gmysql" \  
PDNSCONF_GMYSQL_HOST="db" \  
PDNSCONF_GMYSQL_PORT="3306" \  
PDNSCONF_GMYSQL_DBNAME="pdns" \  
PDNSCONF_GMYSQL_USER="pdns" \  
PDNSCONF_GMYSQL_PASSWORD='' \  
PDNSCONF_GMYSQL_DNSSEC="yes" \  
PDNSCONF_ALLOW_RECURSION="127.0.0.0/8" \  
PDNSCONF_API_KEY=""  
### PDNS ###  
COPY assets/apt/preferences.d/pdns /etc/apt/preferences.d/pdns  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y curl \  
&& curl https://repo.powerdns.com/FD380FBB-pub.asc | sudo apt-key add - \  
&& echo "deb [arch=amd64] http://repo.powerdns.com/ubuntu trusty-auth-40 main"
> /etc/apt/sources.list.d/pdns.list  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
wget \  
git \  
supervisor \  
mysql-client \  
nginx \  
php5-fpm \  
php5-mcrypt \  
php5-mysqlnd \  
pdns-server \  
pdns-backend-mysql \  
&& apt-get clean \  
&& rm /etc/powerdns/pdns.d/*.conf /etc/powerdns/*.conf \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY assets/pdns/pdns.conf /etc/powerdns/pdns.conf  
COPY assets/mysql/pdns.sql /pdns.sql  
  
### PHP/Nginx ###  
COPY assets/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY assets/nginx/vhost.conf /etc/nginx/sites-enabled/vhost.conf  
COPY assets/nginx/fastcgi_params /etc/nginx/fastcgi_params  
  
COPY assets/php/php.ini /etc/php5/fpm/php.ini  
COPY assets/php/php-cli.ini /etc/php5/cli/php.ini  
RUN sed -i -re 's|^error_log\s?=.*|error_log=/proc/self/fd/2|'
/etc/php5/fpm/php-fpm.conf  
  
RUN rm /etc/nginx/sites-enabled/default  
RUN php5enmod mcrypt  
RUN mkdir -p /var/www/html/ \  
&& cd /var/www/html \  
&& git clone https://github.com/cegeka/poweradmin.git . \  
&& git checkout 64cf9a793e9d54734e0a5f2a1e707fa65592558f \  
&& rm -R /var/www/html/install  
  
COPY assets/poweradmin/config.inc.php /var/www/html/inc/config.inc.php  
COPY assets/mysql/poweradmin.sql /poweradmin.sql  
RUN chown -R www-data:www-data /var/www/html/  
  
### SUPERVISOR ###  
COPY assets/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY start.sh /start.sh  
  
EXPOSE 53 80 8081 53/udp  
  
CMD ["/bin/bash", "/start.sh"]  

