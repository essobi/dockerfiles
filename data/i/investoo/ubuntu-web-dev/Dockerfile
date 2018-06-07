FROM ubuntu:16.04  
RUN apt-get update  
  
RUN apt-get install -y \  
curl \  
libssl-dev \  
libxml2-dev \  
libcurl4-openssl-dev \  
pkg-config \  
git \  
vim \  
locate  
  
RUN apt-get install -y \  
php \  
php-gd \  
php-zip \  
php-curl \  
php-iconv \  
php-mcrypt \  
php-bcmath \  
php-mbstring \  
php-dev \  
php-pear \  
php-xdebug \  
php-redis  
  
RUN pecl install mongodb -y  
RUN echo "extension=mongodb.so" >> /etc/php/7.0/cli/conf.d/mongodb.ini  
RUN echo "extension=mongodb.so" >> /etc/php/7.0/fpm/conf.d/mongodb.ini  
  
ADD mongodb.so /usr/lib/php/20151012/mongodb.so  
RUN chmod +x /usr/lib/php/20151012/mongodb.so  
  
RUN curl -s
"https://packagecloud.io/install/repositories/phalcon/stable/script.deb.sh" |
bash  
RUN apt-get install php7.0-phalcon  
  
RUN apt-get install -y \  
php-fpm \  
nginx  
  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash \  
&& apt-get install -y nodejs  
  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& cd /tmp \  
&& php composer-setup.php \  
&& mv composer.phar /usr/bin/composer  
  
RUN service php7.0-fpm start  
  
RUN useradd -rmU -u 1000 appuser  
  
RUN sed -i -e 's/www-data/appuser/g' /etc/php/7.0/fpm/pool.d/www.conf  
RUN sed -i -e 's/www-data/appuser/g' /etc/nginx/nginx.conf  
  
RUN npm install -g webpack aurelia-cli gulp yarn  
  
CMD php-fpm7.0 && nginx -g 'daemon off;'

