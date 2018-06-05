FROM php:7.0-alpine  
  
LABEL maintainer="Albert Colom <skolom@gmail.com>"  
  
RUN apk --update add \  
bash \  
curl \  
git \  
grep \  
openssl-dev \  
openssh-client \  
rsync \  
gzip \  
sudo \  
&& rm -rf /var/cache/apk/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer  
  
WORKDIR /var/www/html

