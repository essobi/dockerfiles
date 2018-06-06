FROM mkodockx/docker-supervisor  
MAINTAINER https://m-ko-x.de Markus Kosmal <code@m-ko-x.de>  
  
ENV DATABASE_NAME pics  
ENV DATABASE_USER picuser  
ENV DATABASE_SECRET "$(pwgen -c -n -1 26)"  
ENV PHP_MAX_UPLOAD 1G  
  
RUN apt-get update -yqq && \  
apt-get install -yqq wget git unzip nginx fontconfig-config fonts-dejavu-core
\  
php5-fpm php5-common php5-json php5-cli php5-common php5-mysql\  
php5-gd php5-json php5-mcrypt php5-readline psmisc ssl-cert \  
ufw php-pear libgd-tools libmcrypt-dev mcrypt mysql-server mysql-client  
  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
RUN service mysql start && \  
mysql -uroot -e "CREATE DATABASE IF NOT EXISTS ${DATABASE_NAME};" && \  
mysql -uroot -e "CREATE USER '${DATABASE_USER}'@'localhost' IDENTIFIED BY
'${DATABASE_SECRET}';" && \  
mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO '${DATABASE_USER}'@'localhost'
WITH GRANT OPTION;" && \  
mysql -uroot -e "FLUSH PRIVILEGES;"  
  
RUN sed -i -e "s/output_buffering\s*=\s*4096/output_buffering = Off/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize =
${PHP_MAX_UPLOAD}/g" /etc/php5/fpm/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = ${PHP_MAX_UPLOAD}/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s:;\s*session.save_path\s*=\s*\"N;/path\":session.save_path =
/tmp:g" /etc/php5/fpm/php.ini  
RUN chown -R www-data:www-data /tmp  
RUN php5enmod mcrypt  
  
RUN mkdir /var/www && \  
chown www-data:www-data /var/www && \  
rm /etc/nginx/sites-enabled/* && \  
rm /etc/nginx/sites-available/*  
  
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 30/"
/etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout 30/keepalive_timeout
30;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
ADD conf/php.conf /etc/nginx/  
ADD conf/lychee /etc/nginx/sites-enabled/  
  
WORKDIR /var/www  
RUN git clone https://github.com/electerious/Lychee.git lychee  
  
RUN chown -R www-data:www-data /var/www/lychee && \  
chmod -R 770 /var/www/lychee && \  
chmod -R 777 /var/www/lychee/uploads/ && \  
chmod -R 777 /var/www/lychee/data/  
  
EXPOSE 80  
WORKDIR /  
RUN ln -s /var/www/lychee/uploads uploads && ln -s /var/www/lychee/data data  
  
VOLUME ["/uploads","/data"]  
  
ADD conf/startup.conf /etc/supervisor/conf.d/  
  
RUN echo "${DATABASE_SECRET}"  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]

