FROM phusion/baseimage:0.9.19  
RUN apt-get update -y  
  
ENV VERSION_CRAFT_MAJOR=2.6  
ENV VERSION_CRAFT_BUILD=2950  
#Using PHP 7.0 instead of PHP5.6  
ENV CRAFT_DEPS=" \  
apache2 \  
curl \  
wget \  
unzip \  
php7.0-cli \  
php7.0-mysql \  
libapache2-mod-php7.0 \  
php7.0-mcrypt \  
php7.0-curl \  
php7.0-gd \  
php-imagick"  
RUN apt-get install -y ${CRAFT_DEPS} \--fix-missing \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /var/www/  
  
COPY ./default.sh /tmp/default.sh  
RUN chmod +x /tmp/default.sh  
RUN /tmp/default.sh  
  
COPY ./init.sh /tmp/init.sh  
RUN chmod +x /tmp/init.sh  
RUN /tmp/init.sh  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ONBUILD RUN rm -R /var/www/craft /var/www/html  
ONBUILD ADD . /var/www  
  
EXPOSE 80  
CMD ["/entrypoint.sh"]  

