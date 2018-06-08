#  
# Build and run:  
#  
# docker build -t php7 .  
# docker run --rm -it php7  
#  
FROM php:7-fpm  
MAINTAINER Mihail Binev <mihail@kodeart.com>  
  
RUN apt-get update && \  
apt-get install -y supervisor libmcrypt-dev libxml2-dev libicu-dev libpq-dev
libsqlite3-dev  
  
# php extensions  
RUN docker-php-ext-install bcmath ctype dom gettext intl json mbstring mcrypt
mysqli opcache pcntl pdo pdo_mysql pdo_pgsql pdo_sqlite simplexml shmop xml
zip  
  
# cleanup  
RUN apt-get -y autoremove && apt-get autoclean && apt-get clean && \  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*  
  
# add conf files for supervisor, php-fpm and php  
ADD config-files /  
  
EXPOSE 9000  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

