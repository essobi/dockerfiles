FROM circleci/php:7.0-apache-node-browsers  
  
MAINTAINER innovatorjapan <system@innovator.jp.net>  
  
RUN sudo apt-get update \  
&& sudo apt-get install -y libpng-dev libjpeg62-turbo-dev \  
&& sudo docker-php-ext-install gd exif pdo_mysql zip  

