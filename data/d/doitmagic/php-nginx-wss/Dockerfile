FROM phusion/baseimage:0.9.17  
MAINTAINER Do IT Magic Software <razvan@doitmagic.com>  
  
#install utilities tools  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends nano zip unzip curl  
  
RUN apt-get install -y --no-install-recommends python-software-properties
software-properties-common  
  
# Update software list, install php-nginx & clear cache  
RUN locale-gen en_US.UTF-8 && \  
export LANG=en_US.UTF-8 && \  
add-apt-repository -y ppa:ondrej/php && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --force-yes --no-install-recommends nginx \  
php5.6 php5.6-zip php5.6-fpm php5.6-cli php5.6-mysql php5.6-mcrypt php5.6-gd
php5.6-xml mysql-client-5.5\  
php5.6-curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
RUN mkdir -p /var/www  
  
RUN mkdir -p /etc/ssl/certs/  
RUN mkdir -p /etc/ssl/private/  
  
COPY ssl/nginx.crt /etc/ssl/certs/  
COPY ssl/nginx.key /etc/ssl/private/  
  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN apt-get autoclean  
  
# Configure nginx  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN sed -i "s/sendfile on/sendfile off/" /etc/nginx/nginx.conf  
  
# Configure PHP  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/"
/etc/php/5.6/cli/php.ini && sed -i "s/;date.timezone =.*/date.timezone =
Europe\/Bucharest/" /etc/php/5.6/cli/php.ini \  
&& sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/5.6/fpm/php-
fpm.conf  
  
##Updated for PHP 5.6  
RUN sed -i "s/pid =.*/pid = \/var\/run\/php-fpm.pid/" /etc/php/5.6/fpm/php-
fpm.conf && sed -i "s/listen =.*sock/listen = \/var\/run\/php-fpm.sock/"
/etc/php/5.6/fpm/pool.d/www.conf  
  
# tweak nginx config  
RUN sed -i "s/worker_processes 1/worker_processes 10/" /etc/nginx/nginx.conf \  
&& sed -i "s/keepalive_timeout\s*65/keepalive_timeout 2/"
/etc/nginx/nginx.conf \  
&& sed -i "s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size
100m/" /etc/nginx/nginx.conf  
  
# tweak php-fpm config  
RUN sed -i "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php/5.6/fpm/php.ini \  
&& sed -i "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php/5.6/fpm/php.ini \  
&& sed -i "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php/5.6/fpm/pool.d/www.conf \  
&& sed -i "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php/5.6/fpm/pool.d/www.conf \  
&& sed -i "s/pm.start_servers = 2/pm.start_servers = 3/g"
/etc/php/5.6/fpm/pool.d/www.conf \  
&& sed -i "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php/5.6/fpm/pool.d/www.conf \  
&& sed -i "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php/5.6/fpm/pool.d/www.conf \  
&& sed -i "s/pm.max_requests = 500/pm.max_requests = 200/g"
/etc/php/5.6/fpm/pool.d/www.conf  
  
RUN phpenmod -v 5.6 mcrypt  
RUN phpenmod -v 5.6 zip  
  
#install composer  
RUN curl -O https://getcomposer.org/composer.phar && mv composer.phar
/usr/local/bin/composer && chmod +x /usr/local/bin/composer  
  
# Add nginx service  
RUN mkdir -p /etc/service/nginx  
ADD build/nginx/run.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run  
  
# Add PHP service  
RUN mkdir -p /etc/service/phpfpm  
ADD build/php/run.sh /etc/service/phpfpm/run  
RUN chmod +x /etc/service/phpfpm/run  
  
#Fixing Permissions  
RUN chown -R www-data:www-data /var/www  
  
# Add nginx volumes  
VOLUME ["/var/www", "/etc/nginx/sites-available", "/etc/nginx/sites-enabled"]  
  
# Set the work directory  
WORKDIR /var/www  
  
# Expose ports  
EXPOSE 80 443 8000

