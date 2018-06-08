FROM php:7.0-alpine  
  
#### docker:1.11 ####  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.11.2  
ENV DOCKER_SHA256
8c2e0c35e3cda11706f54b2d46c2521a6e9026a7b13c7d4b8ae1f3a706fc55e1  
  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v  
  
RUN apk add --no-cache \  
git \  
openssh-client \  
python \  
py-pip \  
zip \  
bash \  
nodejs \  
&& npm install -g yarn \  
&& pip install docker-compose \  
&& pip install awscli --ignore-installed six  
  
#### php composer ####  
ENV PHP_COMPOSER_VERSION 1.2.0  
RUN curl -sS https://getcomposer.org/installer \  
| php -- --install-dir=/usr/local/bin --filename=composer
--version=$PHP_COMPOSER_VERSION  
  
#### xdebug ####  
RUN set -ex \  
&& apk add --no-cache --virtual .xdebug-builddeps \  
autoconf \  
gcc \  
libc-dev \  
make \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& apk del .xdebug-builddeps  
  
#### pdo-mysql ####  
RUN docker-php-ext-install pdo_mysql  
  

