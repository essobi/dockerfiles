FROM php:5.6-cli  
MAINTAINER Sport Archive, Inc.  
  
COPY . /usr/src/cloudpublish  
WORKDIR /usr/src/cloudpublish  
  
RUN echo "date.timezone = UTC" >> /usr/local/etc/php/conf.d/timezone.ini  
RUN DEBIAN_FRONTEND=noninteractive TERM=screen \  
apt-get update \  
&& apt-get install -y git \  
&& apt-get install -y zlib1g-dev autoconf \  
&& docker-php-ext-install zip \  
&& make \  
&& apt-get purge -y git \  
&& apt-get autoremove -y  
  
ENTRYPOINT ["/usr/src/cloudpublish/bootstrap.sh"]  

