FROM php:7.0-fpm-jessie  
  
ENV APP_NAME=NDS-Seismic-Report  
ENV APP_ENV=local  
ENV APP_KEY=base64:5/jLKtqugvjKhzy7z61ZKkIIH/mIqLuROFRkcYxWsqg=  
ENV APP_DEBUG=false  
ENV APP_LOG=daily  
ENV APP_LOG_LEVEL=error  
ENV APP_URL=http://localhost  
  
ENV DB_CONNECTION=mysql  
ENV DB_HOST=report_mysql  
ENV DB_PORT=3306  
ENV DB_DATABASE=homestead  
ENV DB_USERNAME=homestead  
ENV DB_PASSWORD=secret  
  
ENV BROADCAST_DRIVER=log  
ENV CACHE_DRIVER=redis  
ENV SESSION_DRIVER=redis  
ENV QUEUE_DRIVER=redis  
  
ENV REDIS_HOST=redis_nds  
ENV REDIS_PASSWORD=null  
ENV REDIS_PORT=6379  
ENV MAIL_DRIVER=mailgun  
ENV MAIL_HOST=smtp.mailgun.org  
ENV MAIL_PORT=587  
ENV MAIL_USERNAME=null  
ENV MAIL_PASSWORD=null  
ENV MAIL_ENCRYPTION=null  
  
ENV MAILGUN_DOMAIN=cloudnds.com  
ENV MAILGUN_SECRET=key-e027084cf9d6b6806d41ba5ba7d55677  
ENV MAIL_FROM_ADDRESS=no-reply@cloudnds.com  
ENV MAIL_FROM_NAME=cloudnds  
  
ENV PUSHER_APP_ID=  
ENV PUSHER_APP_KEY=  
ENV PUSHER_APP_SECRET=  
  
EXPOSE 9000 9001  
# Copy Start Script  
ADD ./setup/nds-report-start.sh /usr/local/bin/docker-entry.sh  
RUN chmod +x /usr/local/bin/docker-entry.sh  
  
# Copy source code  
COPY ./www /var/www/html/nds-effect-report  
# COPY ./setup/environment /var/www/html/nds-effect-report/.env  
RUN rm -rf /var/www/html/nds-effect-report/storage/logs/laravel.log  
  
# Install Dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libmcrypt-dev \  
mysql-client \  
libmagickwand-dev \  
ca-certificates \  
bzip2 \  
libfontconfig \  
git \  
supervisor \  
unzip \  
git \  
&& pecl install imagick \  
&& docker-php-ext-enable imagick \  
&& docker-php-ext-install mcrypt pdo_mysql  
  
# Setup Supervisor  
RUN mkdir -p /etc/supervisor  
COPY ./setup/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
COPY ./setup/supervisor/task /etc/supervisor/task  
  
# install PhantomJS  
COPY ./setup/phantomjs-2.1.1-linux-x86_64.tar.bz2
/tmp/phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN cd /tmp \  
&& set -x \  
&& tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 \  
&& mv phantomjs-2.1.1-linux-x86_64 /usr/local/share \  
&& ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
/usr/local/bin  
  
# Install PHP Composer + Project PHP Dependecies  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& chmod +x /usr/local/bin/composer \  
&& cd /var/www/html/nds-effect-report \  
&& composer install  
  
# Clear unused file  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp  
  
WORKDIR /var/www/html/nds-effect-report  
VOLUME /var/www/html/nds-effect-report  
  
CMD ["sh","/usr/local/bin/docker-entry.sh"]

