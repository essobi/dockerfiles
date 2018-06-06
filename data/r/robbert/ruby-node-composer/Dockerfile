FROM ubuntu:16.04  
RUN apt-get update  
  
# Install build tools and libraries  
RUN apt-get install -yqq build-essential software-properties-common curl git
python netcat  
  
# Install Apache  
RUN apt-get install -yqq apache2  
  
# Enable mod_rewrite  
RUN a2enmod rewrite  
  
# Install PHP  
RUN apt-get install -yqq php7.0 libapache2-mod-php7.0  
  
# Install PHP extensions  
RUN apt-get install -yqq php7.0-curl php7.0-gd php7.0-json php7.0-opcache
php7.0-mcrypt php7.0-mysql php7.0-sqlite3  
  
# Install ruby  
RUN apt-get install -yqq ruby  
  
# Install Node.js (and fake the distro, as Xenial is currently not supported)  
RUN curl -sL https://deb.nodesource.com/setup_5.x | sed 's/\${DISTRO}/wily/g'
| bash - \  
&& apt-get install -yqq nodejs  
  
# Install the MySQL cli  
RUN apt-get install -yqq mysql-client  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Add composer's vendor directory to the path  
ENV PATH /root/.composer/vendor/bin:$PATH  
  

