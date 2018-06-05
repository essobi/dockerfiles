FROM weyforth/laravel-phpcli  
  
MAINTAINER "Mike Farrow" <contact@mikefarrow.co.uk>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /tmp  
  
RUN apt-get update -y && \  
apt-get install -y \  
php5-mcrypt \  
php5-mongo \  
php5-mssql \  
php5-mysqlnd \  
php5-pgsql \  
php5-redis \  
php5-sqlite \  
php5-gd && \  
php5enmod mcrypt  
  
WORKDIR /data/www  
  
USER "www-data"  
ENTRYPOINT ["php", "artisan"]  
CMD ["--help"]  

