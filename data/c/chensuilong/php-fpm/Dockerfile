FROM php:7.1-fpm  
  
# 设置个时区  
ENV TZ=Asia/Shanghai  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# 设置工作目录  
WORKDIR /var/www/html  
  
#把本地代码copy进去  
#COPY ./app /var/www/html/  
# 不给权限创建不了文件  
#RUN chmod -R 777 /var/www/html/*  
# 设置php-fpm.conf  
COPY php-fpm.conf /usr/local/etc  
  
# 设置php.ini  
COPY php.ini /usr/local/etc/php  
  
# 开放端口  
EXPOSE 9000  
# zip  
RUN apt-get update && apt-get -yqq install zip  
  
# 安装基本拓展  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install opcache  
  
# 安装php扩展 pdo 必备  
RUN docker-php-ext-install pdo pdo_mysql  
  
# 装好vim好调试  
RUN apt-get -yqq install vim  
  
RUN apt-get clean  

