FROM php:5.6-fpm  
RUN apt-get update \  
# 相关依赖必须手动安装  
&& apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
# 安装扩展  
&& docker-php-ext-install -j$(nproc) iconv mcrypt mbstring mysqli pdo
pdo_mysql shmop iconv \  
# 如果安装的扩展需要自定义配置时  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN pecl install redis-4.0.1 \  
&& docker-php-ext-enable redis

