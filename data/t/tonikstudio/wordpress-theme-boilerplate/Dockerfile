FROM alpine:3.6  
  
RUN apk add --no-cache \  
g++ \  
gcc \  
git \  
bash \  
file \  
nasm \  
make \  
automake \  
autoconf \  
gettext \  
libjpeg \  
libpng \  
libpng-dev \  
libtool \  
libnotify \  
&& apk add --update \  
nodejs \  
nodejs-npm \  
&& apk add --update \  
php7 \  
php7-zip \  
php7-json \  
php7-phar \  
php7-openssl \  
php7-mbstring \  
&& rm -rf /tmp/* /var/cache/apk/* \  
&& ln -nfs /usr/bin/php7 /usr/bin/php \  
&& ln -nfs /etc/php7 /etc/php  
  
COPY --from=composer:1.6 /usr/bin/composer /usr/bin/composer  
  
CMD ["php", "composer", "npm"]  

