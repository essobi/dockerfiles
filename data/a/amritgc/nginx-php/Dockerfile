FROM ubuntu:xenial  
  
LABEL MAINTAINER="Amrit G.C. <music.demand01@gmail.com>"  
RUN useradd -ms /bin/bash -u 1337 amritgc  
  
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >
/etc/apt/sources.list.d/ppa_ondrej_php.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C \  
&& apt-get update  
  
RUN apt-get install -y curl zip unzip git supervisor sqlite3 nginx \  
php7.1 \  
php7.1-fpm \  
php7.1-cli \  
php7.1-bcmath \  
php7.1-bz2 \  
php7.1-imap \  
php7.1-common \  
php7.1-mbstring \  
php7.1-json \  
php7.1-gd \  
php7.1-intl \  
php7.1-mysql \  
php7.1-json \  
php7.1-opcache \  
php7.1-curl \  
php7.1-xdebug \  
php7.1-zip \  
php7.1-xml \  
php7.1-sqlite3 \  
&& echo "daemon off;" >> /etc/nginx/nginx.conf  
  
RUN apt-get -y autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN sed -i '/;daemonize /c \  
daemonize = no' /etc/php/7.1/fpm/php-fpm.conf  
  
RUN sed -i '/^listen /c \  
listen = 0.0.0.0:9000' /etc/php/7.1/fpm/pool.d/www.conf  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
WORKDIR /var/www/  
  
EXPOSE 80  
CMD service php7.1-fpm start && nginx  

