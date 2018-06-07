FROM php:5.5-fpm  
  
RUN apt-get update  
  
RUN apt-get install -y php5-dev  
RUN apt-get install -y nano git  
  
RUN apt-get install -y libmcrypt-dev && docker-php-ext-install -j$(nproc)
mcrypt pdo pdo_mysql;  
  
RUN apt-get install -y libmemcached-dev zlib1g-dev graphviz \  
&& pecl install memcached-2.2.0 \  
&& docker-php-ext-enable memcached  
  
# Install bcmath  
RUN docker-php-ext-install bcmath  
  
RUN apt-get install -y zlib1g-dev && docker-php-ext-install zip  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
# parallel install plugin  
RUN composer global require hirak/prestissimo  
  
# install xhprof  
RUN pecl install xhprof-0.9.4  
RUN mkdir /var/xhprof \  
&& tar -xf /tmp/pear/download/xhprof-0.9.4.tgz -C /tmp \  
&& cp -R /tmp/xhprof-0.9.4/. /var/xhprof  
COPY ./xhprof/*.php /var/xhprof/  
VOLUME /var/xhprof  
  
RUN apt-get clean && apt-get autoclean && apt-get autoremove -y  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN mkdir /var/tmp/xhprof && chmod 777 /var/tmp/xhprof  
  
ADD ./conf.d/*.ini /usr/local/etc/php/conf.d/  
  
ADD ./php-fpm.d/www.conf /usr/local/etc/php-fpm.d/www.conf  
  
WORKDIR /var/www  
  
EXPOSE 9000

