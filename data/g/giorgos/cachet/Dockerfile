FROM debian:jessie  
  
MAINTAINER Giorgos Logiotatidis <giorgos@sealabs.net>  
  
RUN apt-get update && apt-get -y --no-install-recommends install \  
nginx ca-certificates php5-fpm=5.* php5-curl php5-readline php5-mcrypt \  
php5-mysql php5-apcu php5-cli php5-gd php5-mysql php5-pgsql php5-sqlite \  
wget sqlite git libsqlite3-dev postgresql-client mysql-client curl \  
supervisor cron unzip gettext-base python-pip && \  
apt-get clean && apt-get autoremove -q && \  
rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man /tmp/*  
  
RUN pip install supervisor-stdout  
  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-
fpm.conf  
  
WORKDIR /var/www/html/  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
  
ENV CACHET_VERSION v2.2.4  
RUN wget https://github.com/cachethq/Cachet/archive/${CACHET_VERSION}.tar.gz
&& \  
tar xzvf ${CACHET_VERSION}.tar.gz --strip-components=1 && \  
chown -R www-data /var/www/html && \  
rm -r ${CACHET_VERSION}.tar.gz && \  
php composer.phar install --no-dev -o && \  
rm -rf bootstrap/cache/*  
  
COPY conf/supervisord.conf /etc/supervisor/supervisord.conf  
COPY conf/php-fpm-pool.conf /etc/php5/fpm/pool.d/www.conf  
COPY conf/nginx.conf /nginx.conf  
COPY conf/env.docker /var/www/html/env.docker  
COPY conf/crontab /etc/cron.d/artisan-schedule  
COPY conf/entrypoint.sh /entrypoint.sh  
  
RUN touch .env  
  
RUN chmod 0644 /etc/cron.d/artisan-schedule &&\  
touch /var/log/cron.log  
  
EXPOSE 5000  
CMD ["/entrypoint.sh"]  

