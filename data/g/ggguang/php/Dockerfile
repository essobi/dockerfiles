#  
# 安装 php composer  
#  
# 镜像 php:7.1-fpm  
FROM php:7.1-fpm  
  
# 更换阿里云的apt-get源  
RUN cat /etc/apt/sources.list \  
&& mv /etc/apt/sources.list /etc/apt/sources.list.backup \  
&& touch /etc/apt/sources.list \  
&& echo 'deb http://mirrors.aliyun.com/debian/ jessie main non-free contrib'
>> /etc/apt/sources.list \  
&& echo 'deb http://mirrors.aliyun.com/debian/ jessie-proposed-updates main
non-free contrib' >> /etc/apt/sources.list \  
&& echo 'deb-src http://mirrors.aliyun.com/debian/ jessie main non-free
contrib' >> /etc/apt/sources.list \  
&& echo 'deb-src http://mirrors.aliyun.com/debian/ jessie-proposed-updates
main non-free contrib' >> /etc/apt/sources.list \  
&& echo "`cat /etc/apt/sources.list.backup`" >> /etc/apt/sources.list \  
&& cat /etc/apt/sources.list  
  
# 更新 apt-get 与 安装多线程下载工具 axel  
RUN apt-get update && apt-get install -y axel  
  
# 安装 git subversion 版本管理 与 zip upzip 加解压缩 工具  
RUN apt-get install -y --no-install-recommends git subversion zip unzip  
  
# 安装 php composer  
RUN axel https://getcomposer.org/download/1.4.2/composer.phar \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer  
  
# 安装 phpunit  
RUN curl -fSL https://phar.phpunit.de/phpunit-6.1.phar -o phpunit.phar \  
&& mv phpunit.phar /usr/local/bin/phpunit \  
&& chmod +x /usr/local/bin/phpunit  
  
# 安装 php 扩展 redis  
RUN pecl install redis && docker-php-ext-enable redis  
  
# 安装 php 扩展 mongodb，debain.libssl-dev=centos.openssl-devel  
RUN apt-get install -y openssl libssl-dev && pecl install mongodb && docker-
php-ext-enable mongodb  
  
# 安装 php 扩展 memcached  
RUN apt-get install -y libmemcached-dev zlib1g-dev \  
&& pecl install memcached && docker-php-ext-enable memcached  
  
# 安装 php 扩展 iconv mcrypt gd  
RUN apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
&& docker-php-ext-install -j$(nproc) iconv \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
#  
# 安装 php 扩展 xhprof，configure --with-php-config=/usr/local/bin/php-config  
#  
# pecl.php.net 的 xhprof 没有 stable 版，最后版本 xhprof-0.9.4.tgz 是 2013-09-30 更新  
#  
# pecl php7 install 报错 error: 'zval' has no member named 'type'  
#  
# RUN pecl install xhprof-0.9.4 && docker-php-ext-enable xhprof  
RUN cd ~ \  
&& git clone https://github.com/longxinH/xhprof.git ./xhprof \  
&& cd ./xhprof/extension/ \  
&& phpize \  
&& ./configure --with-php-config=/usr/local/bin/php-config \  
&& make && make install \  
&& mkdir -p /php/xhprof/data \  
&& cd /usr/local/etc/php/conf.d \  
&& touch docker-php-ext-xhprof.ini \  
&& echo "extension = xhprof.so" >> docker-php-ext-xhprof.ini \  
&& echo "xhprof.output_dir = /php/xhprof/data" >> docker-php-ext-xhprof.ini \  
&& cd ~ \  
&& rm -rf xhprof  
  
# 安装 php 扩展 pdo_mysql  
RUN docker-php-ext-install pdo_mysql  
  
# 开启 php-fpm 错误日志  
#RUN mkdir -p /php/log/ \  
# && chmod 777 /php/log \  
# && cd /usr/local/etc \  
# && mv php-fpm.conf php-fpm.conf.backup \  
# && sed 's!;error_log = log/php-fpm.log!error_log = /php/log/php-
fpm.error.log!g' php-fpm.conf.backup | tee php-fpm.conf > /dev/null  
# 开启 php 错误日志  
#RUN cd /usr/local/etc/php/conf.d \  
# && touch docker-php-error-log.ini \  
# && echo 'error_log = /php/log/php.error.log' >> docker-php-error-log.ini  
#  
# docker image php:7.1-fpm 已经开放端口 9000  
#  
# RUN rm -r /var/lib/apt/lists/*  
#  
# EXPOSE 9000  
#  
# CMD ["php-fpm"]  
#

