FROM php:7-fpm-alpine3.7  
MAINTAINER coolyaolei<coolyaolei@sina.com>  
  
#ENV TZ=Asia/Shanghai  
USER root  
  
# Change mirror site For China  
#RUN echo 'https://mirror.tuna.tsinghua.edu.cn/alpine/v3.7/main' >
/etc/apk/repositories \  
# && echo 'https://mirror.tuna.tsinghua.edu.cn/alpine/v3.7/community' >>
/etc/apk/repositories \  
RUN apk add --update --no-cache freetype-dev libjpeg-turbo-dev libmcrypt-dev
libpng-dev postgresql-dev\  
&& docker-php-ext-install mysqli pdo pdo_mysql pdo_pgsql \  
&& docker-php-ext-install gd \  
&& docker-php-source delete \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
EXPOSE 9000  
CMD ["php-fpm"]  

