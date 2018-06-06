FROM circleci/php:5.6-apache-node-browsers  
  
MAINTAINER Whiteaway Dev <dev@whiteaway.com>  
  
RUN curl -sS https://getcomposer.org/installer \  
| sudo php -- --install-dir=/usr/local/bin --filename=composer \  
&& sudo chmod +x /usr/local/bin/composer  
  
RUN sudo apt-get update \  
&& sudo apt-get install -y python3-pip \  
&& sudo pip3 install awscli  
  
RUN npm config set progress false \  
&& npm config set color false \  
&& npm config set unicode false \  
&& npm config set spin false \  
&& npm config set registry http://registry.npmjs.org/ \  
&& sudo npm install -g gulp \  
&& sudo npm install -g bower

