FROM ubuntu:14.04  
MAINTAINER lucienchu<lucienchu@hotmail.com>  
  
#RUN sed -Ei
'1,$s/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/cn.archive.ubuntu.com\/ubuntu\//g'
/etc/apt/sources.list \  
RUN apt-get update -q \  
&& apt-get upgrade -y \  
&& apt-get install -y php5-mysql \  
nginx \  
php5-fpm \  
curl \  
wget \  
git \  
php5-cli \  
php5-gd \  
php5-mcrypt \  
nodejs \  
nodejs-legacy \  
mysql-client  
  
VOLUME /data  
WORKDIR /var/www/  
  
# php extension  
RUN ln -s /etc/php5/mods-available/mcrypt.ini /etc/php5/fpm/conf.d/ \  
&& ln -s /etc/php5/mods-available/mcrypt.ini /etc/php5/cli/conf.d/  
  
# comoposer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# paperwork  
RUN git clone https://github.com/twostairs/paperwork.git \  
&& cd /var/www/paperwork/frontend/ \  
&& composer install  
  
# npm  
RUN cd /var/www/paperwork/frontend/ \  
&& wget https://www.npmjs.org/install.sh \  
&& bash ./install.sh \  
&& npm install -g gulp bower \  
&& npm install \  
&& bower install --allow-root \  
&& gulp  
  
COPY docker-entrypoint.sh /usr/local/bin/  
COPY paperwork.conf /etc/nginx/sites-available/  
COPY database.json /var/www/paperwork/frontend/app/storage/config/  
COPY crontab /etc/cron.d/  
  
RUN rm -f /etc/nginx/sites-enabled/default \  
&& ln -s /etc/nginx/sites-available/paperwork.conf /etc/nginx/sites-enabled/  
  
ENTRYPOINT ["docker-entrypoint.sh"]

