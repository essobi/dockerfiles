FROM php:5.6-cli  
  
MAINTAINER Romain THERRAT <romain42@gmail.com>  
  
RUN buildDeps="\  
git \  
"\  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install mysql pdo_mysql  
  

