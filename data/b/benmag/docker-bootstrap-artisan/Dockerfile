FROM ubuntu:trusty  
  
MAINTAINER Ben M, git@bmagg.com  
  
# Install packages  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -yq install curl
apache2 libapache2-mod-php5 \  
php-pear \  
php-apc \  
php5-curl \  
php5-gd \  
php5-mcrypt \  
php5-pgsql \  
php5-mongo \  
php5-mssql \  
php5-redis \  
php5-sqlite  
RUN rm -rf /var/lib/apt/lists/*  
  
# Install mcrypt  
RUN php5enmod mcrypt  
  
# Restart apache  
RUN service apache2 restart  
  
# Mount  
VOLUME /app  
WORKDIR /app  
  
# Set up entry points  
ENTRYPOINT ["php", "artisan"]  
CMD ["--help"]  

