FROM php:5.6  
MAINTAINER Lopez Shackleford <lopez.shackleford@gmail.com>  
  
# Install packages  
RUN apt-get update && apt-get install -y --no-install-recommends \  
git \  
wget \  
zip \  
libpng-dev \  
zlib1g-dev && \  
rm -r /var/lib/apt/lists/*  
  
RUN docker-php-ext-install mbstring \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install zip  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# @TODO set up apache/mysql ennvironment for drush testing  
# Jenkins is run with user `jenkins`, uid = 1000  
RUN useradd -d /home/jenkins -u 1000 -m -s /bin/bash jenkins  
  
USER jenkins

