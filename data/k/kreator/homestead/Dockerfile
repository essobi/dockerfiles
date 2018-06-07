FROM php:7.1-fpm  
  
LABEL maintainer="gfx@karpiak.pl"  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libicu-dev \  
libxml2-dev \  
git \  
unzip \  
nano \  
beanstalkd \  
supervisor \  
cron \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN docker-php-ext-install opcache intl pdo_mysql mbstring bcmath  
  
RUN export TERM=xterm  
RUN echo 'alias ll="ls --color=auto -la"' >> ~/.bashrc \  
&& echo 'alias phpunit="vendor/bin/phpunit"' >> ~/.bashrc \  
&& echo 'alias artisan="php ./artisan"' >> ~/.bashrc  
  
EXPOSE 11300/TCP  
  
WORKDIR /opt/app/  
  
COPY crontab /var/crontab  
RUN crontab /var/crontab && touch /var/log/cron.log && cron  
  
CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf ; php-fpm

