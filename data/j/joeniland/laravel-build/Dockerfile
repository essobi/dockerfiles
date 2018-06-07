FROM alpine:edge  
  
MAINTAINER Joe Niland <joe@originalmind.com.au>  
  
RUN set -x \  
&& apk update \  
&& apk add \  
build-base \  
autoconf \  
automake \  
zip \  
unzip \  
nasm \  
bash \  
php7 \  
php7-xml \  
php7-zip \  
php7-xmlreader \  
php7-xmlwriter \  
php7-zlib \  
php7-opcache \  
php7-mcrypt \  
php7-openssl \  
php7-curl \  
php7-fileinfo \  
php7-json \  
php7-dom \  
php7-phar \  
php7-mbstring \  
php7-bcmath \  
php7-pdo \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-pdo_mysql \  
php7-soap \  
php7-pcntl \  
php7-gd \  
php7-tokenizer \  
python2 \  
git \  
nodejs-current-npm \  
libpng-dev \  
rsync \  
openssh-client  
  
RUN npm install --silent -g \  
gulp-cli \  
bower \  
yarn  
RUN yarn global add node-sass  
  
WORKDIR /tmp  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php --install-dir=/usr/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');"  
  
VOLUME ["/app"]  
WORKDIR /app  
  

