FROM php:7.1-alpine  
MAINTAINER Tobias Kuendig <tobias@offline.swiss>  
  
RUN echo -e 'http://dl-cdn.alpinelinux.org/alpine/edge/main\nhttp://dl-
cdn.alpinelinux.org/alpine/edge/community\nhttp://dl-
cdn.alpinelinux.org/alpine/edge/testing' > /etc/apk/repositories  
  
RUN apk add --no-cache \  
ca-certificates \  
curl \  
zip \  
file \  
yarn \  
openssl \  
openssh-client \  
coreutils \  
freetype-dev \  
libjpeg-turbo-dev \  
libltdl \  
libmcrypt-dev \  
libpng-dev \  
&& rm -rf /var/cache/apk/*  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN docker-php-ext-install zip  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer && chmod +x
/usr/local/bin/composer  
  
# Docker  
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
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["sh"]  

