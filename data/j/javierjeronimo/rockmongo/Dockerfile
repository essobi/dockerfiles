FROM ubuntu:14.04  
MAINTAINER Javier Jerónimo <javier@jeronimosuarez.es>  
  
# Hostname in nginx-site (useful in panamax ==> non "localhost")  
ENV NGINX_HOSTNAME rockmongo.docker.local  
  
# rockmongo config.php  
ENV MONGO_NAME mongo  
ENV MONGO_HOSTNAME mongo  
ENV MONGO_PORT 27017  
RUN apt-get update && \  
apt-get install -y --no-install-recommends build-essential wget nginx php5-fpm
php-pear php5-dev && \  
printf "\n" | pecl install mongo && \  
apt-get remove -yq --purge php5-dev build-essential php-pear && \  
apt-get autoremove -yq --purge && \  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* && \  
echo "extension=mongo.so" > /etc/php5/mods-available/mongo.ini && php5enmod
mongo && \  
sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php5/fpm/php.ini
&& \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php5/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
&& \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php5/fpm/pool.d/www.conf  
  
RUN mkdir -p /var/lib/php5/sessions && \  
chown www-data:www-data /var/lib/php5/sessions && \  
chmod 777 /var/lib/php5/sessions && \  
echo "php_value[session.save_path] = /var/lib/php5/sessions" >>
/etc/php5/fpm/pool.d/www.conf && \  
echo "daemon off;" >> /etc/nginx/nginx.conf && \  
mkdir /app && \  
cd /app && \  
wget --no-check-certificate
https://github.com/iwind/rockmongo/archive/1.1.7.tar.gz && \  
tar -zxvf 1.1.7.tar.gz && \  
mv rockmongo-1.1.7/* . && \  
rm 1.1.7.tar.gz && rmdir rockmongo-1.1.7 && \  
echo "<?php phpinfo(); " > /app/info.php  
  
EXPOSE 80  
ADD ./rockmongo.conf /etc/nginx/sites-available/default  
RUN sed -i -e "s/%%%NGINX_HOSTNAME%%%/${NGINX_HOSTNAME}/g" /etc/nginx/sites-
available/default  
  
RUN cat /etc/nginx/sites-available/default  
  
ADD ./config.php /app/config.php  
RUN sed -i -e "s/%%%MONGO_NAME%%%/${MONGO_NAME}/g" /app/config.php  
RUN sed -i -e "s/%%%MONGO_HOSTNAME%%%/${MONGO_HOSTNAME}/g" /app/config.php  
RUN sed -i -e "s/%%%MONGO_PORT%%%/${MONGO_PORT}/g" /app/config.php  
  
RUN cat /app/config.php  
  
CMD service php5-fpm start && nginx  

