FROM ubuntu:xenial  
MAINTAINER Leen <leen@leen.in>  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update  
  
RUN apt-get -y install \  
software-properties-common \  
python-software-properties  
  
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php  
  
RUN apt-get update  
  
RUN apt-get -y install \  
git \  
curl \  
zip \  
wget \  
unzip \  
php7.1 \  
php7.1-xml \  
php7.1-mbstring \  
php7.1-mysql \  
php7.1-gd \  
php7.1-curl \  
php7.1-redis \  
php7.1-fpm \  
php7.1-zip  
  
RUN wget http://nginx.org/keys/nginx_signing.key  
  
RUN apt-key add nginx_signing.key  
  
RUN rm -rf nginx_signing.key  
  
RUN echo 'deb http://nginx.org/packages/ubuntu/ '$(lsb_release -cs)' nginx' >
/etc/apt/sources.list.d/nginx.list  
  
RUN apt-get update && apt-get -y install nginx  
  
RUN apt-get clean  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN mkdir -p /app && rm -fr /usr/share/nginx/html && ln -s /app
/usr/share/nginx/html  
  
RUN rm -rf /etc/nginx/conf.d/default.conf  
ADD nginx.conf /etc/nginx/conf.d/default.conf  
  
RUN sed -i "s/user nginx;/user www-data;/g" /etc/nginx/nginx.conf  
  
RUN mkdir /var/run/php  
  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
WORKDIR /app  
  
ONBUILD ADD . /app  
ONBUILD RUN composer install --no-dev  
ONBUILD RUN chown www-data:www-data /app -R  
  
EXPOSE 80  
CMD ["/run.sh"]  

