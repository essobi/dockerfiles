FROM datravel/php-fpm:5.6  
ENV PATH=/bin:/usr/bin:/sbin:/usr/sbin  
ENV TERM=xterm  
ENV DEBIAN_FRONTEND=editor  
ENV EDITOR=nano  
  
WORKDIR /var/www/pinboard  
  
RUN mkdir -p /var/www/pinboard  
  
RUN apt-get update \  
&& apt-get install -y nano dialog cron git nginx \  
&& apt-get clean  
  
RUN git clone https://github.com/intaro/pinboard.git /var/www/pinboard  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
\  
&& mv /usr/bin/composer.phar /usr/bin/composer  
  
RUN cd /var/www/pinboard && \  
composer install --no-interaction && \  
composer update kurl/silex-doctrine-migrations-provider doctrine/migrations  
  
RUN apt-get remove -y git \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY ./run.php /var/www/pinboard/web/  
COPY ./parameters.yml /var/www/pinboard/config/parameters.yml  
COPY ./php.ini /etc/php5/fpm/conf.d/99-custom.ini  
COPY ./fpm-pool.conf /etc/php5/fpm/pool.d/www.conf  
COPY ./pinboard.nginx.conf /etc/nginx/sites-enabled/pinboard.conf  
  
CMD service nginx start \  
&& service cron start \  
&& ./console migrations:migrate --no-interaction \  
&& ./console register-crontab --no-interaction \  
&& exec /usr/sbin/php5-fpm -F  

