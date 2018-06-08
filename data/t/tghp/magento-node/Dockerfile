FROM php:7.1-cli  
MAINTAINER TGHP <glasshouse@tghp.co.uk>  
  
RUN apt-get update && apt-get install -y \  
cron \  
git \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev \  
mysql-client \  
vim \  
zip  
  
RUN docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/  
  
RUN docker-php-ext-install \  
bcmath \  
gd \  
intl \  
mbstring \  
mcrypt \  
opcache \  
pdo_mysql \  
soap \  
xsl \  
zip  
  
RUN apt-get update \  
&& apt-get install -y curl gnupg2 build-essential \  
&& curl -sL https://deb.nodesource.com/setup_9.x | bash - \  
&& apt-get install -y nodejs  
  
RUN npm install -g grunt-cli  
  
COPY bin/run-grunt-all /usr/local/bin/  
COPY bin/run-grunt-theme /usr/local/bin/  
  
WORKDIR /var/www/html  
  
CMD ["/bin/bash"]  

