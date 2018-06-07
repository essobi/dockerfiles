FROM php:7.1-fpm  
  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install opcache  
  
RUN echo 'deb http://mirrors.aliyun.com/debian/ jessie main non-free contrib'
> /etc/apt/sources.list \  
&& echo 'deb http://mirrors.aliyun.com/debian/ jessie-proposed-updates main
non-free contrib' >> /etc/apt/sources.list \  
&& echo 'deb-src http://mirrors.aliyun.com/debian/ jessie main non-free
contrib' >> /etc/apt/sources.list \  
&& echo 'deb-src http://mirrors.aliyun.com/debian/ jessie-proposed-updates
main non-free contrib' >> /etc/apt/sources.list  
  
RUN apt-get update \  
&& apt-get install -y nodejs  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  

