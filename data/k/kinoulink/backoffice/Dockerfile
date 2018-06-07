FROM phusion/baseimage:0.9.19  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN apt-get update && \  
apt-get install -y net-tools make \  
php php-curl php-zip php-pdo php-gd php-xml php-apcu php-mysql php-sqlite3
php-intl wget curl \  
nginx-light && \  
apt-get clean  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN mkdir /run/php /etc/service/nginx /etc/service/php  
  
ADD services/nginx /etc/service/nginx/run  
ADD services/php /etc/service/php/run  
ADD services/cron /etc/cron.d/ktv  
ADD services/init /etc/my_init.d/install  
ADD services/install /opt/ktv/bin/install  
ADD services/functions /opt/ktv/bin/functions  
  
RUN echo "source /opt/ktv/bin/functions" >> ~/.bashrc  
  
RUN mkdir -p /opt/ktv/fs/cache /var/lib/php/session && \  
chown www-data:www-data -R /opt/ktv /var/lib/php/session && \  
chmod 600 /etc/cron.d/ktv && \  
chmod 755 /opt/ktv/bin/*  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD php.ini /etc/php/7.0/fpm/php.ini  
ADD php.ini /etc/php/7.0/cli/php.ini  
ADD php_fpm.conf /etc/php/7.0/fpm/php-fpm.conf  
ADD php_fpm_pool.conf /etc/php/7.0/fpm/pool.d/www.conf  
  
RUN rm -rf /etc/service/sshd && \  
rm -rf /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
ENV COMPOSER_HOME /opt/ktv/composer  
  
VOLUME /opt/ktv/composer/cache  
VOLUME /opt/ktv/volume  
  
EXPOSE 80  

