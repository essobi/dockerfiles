FROM debian:stretch  
  
MAINTAINER eball@ccctechcenter.org  
  
WORKDIR /tmp  
  
RUN apt-get update -y && \  
apt-get install -y \  
php7.0-cli \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-pgsql \  
php-redis \  
php-mongodb \  
php7.0-sqlite3 \  
php7.0-dev \  
make \  
php-pear \  
php7.0-gd && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /var/www  
VOLUME ["/var/www"]  
WORKDIR /var/www  
  
EXPOSE 3306  
ENTRYPOINT ["php", "artisan"]  
CMD ["--help"]  

