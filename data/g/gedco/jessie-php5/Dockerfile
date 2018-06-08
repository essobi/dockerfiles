#  
# Debian Jessie + php5-fpm base dev & test image.  
#  
# Build: docker build -t local:jessie-php5 --pull --rm .  
# Usage: docker run --name php5-testapp -d -it local:jessie-php5 bash  
# Clean: docker stop php5-testapp  
#  
FROM debian:jessie  
  
# Mark this system as noninteractive.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install and configure all the software.  
RUN apt-get update; \  
apt-get --yes upgrade; \  
apt-get install --yes --no-install-recommends less nano curl php5-fpm
php5-curl php5-pgsql; \  
apt-get clean  
  
# PHP-FPM configuration  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-
fpm.conf; \  
sed -i -e "s/error_log\s*=\s*\/var\/log\/php5-fpm.log/error_log =
\/proc\/self\/fd\/2/g" /etc/php5/fpm/php-fpm.conf; \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/fpm/php.ini; \  
sed -i -e
"s/;always_populate_raw_post_data\s*=\s*-1/always_populate_raw_post_data =
-1/g" /etc/php5/fpm/php.ini; \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php5/fpm/php.ini; \  
sed -i -e "s/listen\s*=\s*\/var\/run\/php5-fpm.sock/listen = 9000/g"
/etc/php5/fpm/pool.d/www.conf; \  
sed -i -e "s/;pm.status_path\s*=\s*\/status/pm.status_path = \/status/g"
/etc/php5/fpm/pool.d/www.conf; \  
sed -i -e "s/;ping.path\s*=\s*\/ping/ping.path = \/ping/g"
/etc/php5/fpm/pool.d/www.conf; \  
sed -i -e "s/;access.log\s*=\s*log\/\$pool.access.log/access.log =
\/proc\/self\/fd\/1/g" /etc/php5/fpm/pool.d/www.conf; \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php5/fpm/pool.d/www.conf; \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php5/fpm/pool.d/www.conf; \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g"
/etc/php5/fpm/pool.d/www.conf; \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php5/fpm/pool.d/www.conf; \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php5/fpm/pool.d/www.conf; \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g"
/etc/php5/fpm/pool.d/www.conf  
  
# Install PHP Composer  
RUN curl -skS https://getcomposer.org/installer | php5 -- --install-
dir=/usr/local/bin --filename=composer  
# Iniciar el servidor PHP.  
ENTRYPOINT ["php5-fpm", "-F", "-O"]  
  
# Expose related ports.  
EXPOSE 9000  

