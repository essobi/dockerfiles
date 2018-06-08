FROM php:7.1-cli  
  
RUN apt-get update \  
&& apt-get install \  
libxml2-dev \  
&& docker-php-ext-install xmlrpc \  
&& apt-get -y install \  
git-core \  
ssh-client \  
zip \  
unzip \  
&& apt-get install -y libicu-dev \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install pdo pdo_mysql  
  

