FROM php  
  
MAINTAINER serkin.alexander@gmail.com  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y git libssl-dev
wget  
  
RUN docker-php-ext-install zip \  
&& docker-php-ext-install mbstring  
  
COPY . /var/src  
WORKDIR /var/src  
  
# Install Composer  
ENV COMPOSER_VERSION 1.2.0  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer --version=${COMPOSER_VERSION}  
  
# Install Deployer  
RUN wget http://deployer.org/deployer.phar  
RUN mv deployer.phar /usr/local/bin/dep  
RUN chmod +x /usr/local/bin/dep  

