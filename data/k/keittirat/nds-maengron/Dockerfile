FROM keittirat/nds-php5:5-fpm  
# FROM php:7.1.7-fpm  
ENV LANG en_GB.UTF-8  
RUN mkdir /web  
RUN mkdir /web/maengron  
WORKDIR /web/maengron  
  
COPY . /web/maengron  
RUN rm -rf /web/maengron/setup  
  
RUN cd /tmp && curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
# RUN docker-php-source extract  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -o Dpkg::Options::="--force-confold" \--force-yes -y cron  
RUN apt-get install -y git \  
gettext \  
python \  
nodejs  
  
# libmcrypt-dev  
# php5-imagick  
# RUN apt-get install -y \  
# libmagickwand-dev --no-install-recommends  
# RUN docker-php-ext-install \  
# mcrypt \  
# mysqli \  
# zip \  
# pdo_mysql \  
# gettext \  
# bz2 \  
# gd  
# RUN pecl install imagick && docker-php-ext-enable imagick  
# RUN pecl install imagick-beta && docker-php-ext-enable imagick  
RUN cd /web/maengron && npm install gulp -g && npm install && gulp
--production && npm prune --production  
RUN npm uninstall gulp -g && apt-get autoremove -y nodejs git python  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY setup/crond.txt /var/spool/cron/crontabs/root  
RUN chmod 755 /var/spool/cron/crontabs/root  
RUN crontab /var/spool/cron/crontabs/root  
  
VOLUME /web/maengron  
  
CMD ["php-fpm","-F"]  

