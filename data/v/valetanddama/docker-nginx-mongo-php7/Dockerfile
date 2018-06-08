FROM ubuntu:latest  
  
MAINTAINER Alexander<valetanddama@gmail.com>  
  
ENV HOME /root  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
  
#install mongo  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 && \  
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list && \  
apt-get update && \  
apt-get install -y mongodb-org  
  
#install php7  
RUN apt-get -y install software-properties-common python-software-properties  
RUN apt-get update  
RUN apt-get -y install php7.0 php7.0-fpm php7.0-mysql php7.0-curl
php7.0-mcrypt php7.0-cli php7.0-dev php-pear libsasl2-dev  
RUN mkdir -p /usr/local/openssl/include/openssl/ && \  
ln -s /usr/include/openssl/evp.h /usr/local/openssl/include/openssl/evp.h && \  
mkdir -p /usr/local/openssl/lib/ && \  
ln -s /usr/lib/x86_64-linux-gnu/libssl.a /usr/local/openssl/lib/libssl.a && \  
ln -s /usr/lib/x86_64-linux-gnu/libssl.so /usr/local/openssl/lib/  
RUN pecl install mongodb  
RUN echo "extension=mongodb.so" > /etc/php/7.0/fpm/conf.d/20-mongodb.ini && \  
echo "extension=mongodb.so" > /etc/php/7.0/cli/conf.d/20-mongodb.ini && \  
echo "extension=mongodb.so" > /etc/php/7.0/mods-available/mongodb.ini  
  
#install nginx  
COPY ./files/nginx-php7.conf /etc/nginx/sites-available/nginx-php7.conf  
RUN nginx=stable && \  
add-apt-repository ppa:nginx/$nginx && \  
apt-get update && \  
apt-get install -y nginx && \  
rm -Rf /etc/nginx/sites-enabled/default && \  
ln -s /etc/nginx/sites-available/nginx-php7.conf /etc/nginx/sites-
enabled/default  
  
RUN rm -rf /var/www  
RUN mkdir -p /var/www/public_html  
RUN mkdir -p /data/db  
  
WORKDIR /var/www/public_html  
VOLUME ["/var/www/public_html"]  
  
ADD ./files/start.sh /start.sh  
RUN chmod +x /start.sh && \  
mkdir /run/php  
  
EXPOSE 80  
EXPOSE 27017  
CMD /start.sh  
  

