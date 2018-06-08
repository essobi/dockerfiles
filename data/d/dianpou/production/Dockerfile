FROM dianpou/ubuntu  
  
MAINTAINER Garbin Huang <garbinh@gmail.com>  
  
# Nginx  
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu $(lsb_release -sc)
main" && \  
tee /etc/apt/sources.list.d/nginx-stable.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C  
  
# PHP  
RUN add-apt-repository ppa:ondrej/php5-5.6  
  
RUN apt-get update  
RUN apt-get -y --force-yes upgrade  
RUN apt-get install -y --force-yes nginx php5-fpm php5-mcrypt php5-sqlite
php5-cli php5-xcache php5-curl php5-json php5-gd php5-geoip php5-imagick
php5-ldap php5-mysql php5-oauth php5-pgsql php5-redis  
  
# Config  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN sed -i -e "s/short_open_tag = Off/short_open_tag = On/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/post_max_size = 8M/post_max_size = 20M/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/upload_max_filesize = 2M/upload_max_filesize = 20M/g"
/etc/php5/fpm/php.ini  
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php5/fpm/php.ini  
RUN echo "max_input_vars = 10000;" >> /etc/php5/fpm/php.ini  
RUN mkdir /var/www  
RUN echo "<?php phpinfo();" >> /var/www/index.php  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
COPY supervisor/conf.d/* /etc/supervisor/conf.d/  
COPY nginx_default_site /etc/nginx/sites-available/default  
  
VOLUME ["/etc/nginx", "/etc/php5", "/var/www"]  
  
CMD supervisord -n  

