FROM alpine:3.7  
  
WORKDIR /tmp  
  
RUN apk --no-cache add \  
alpine-sdk \  
autoconf \  
autoconf \  
automake \  
bash \  
build-base \  
ca-certificates \  
curl \  
file \  
git \  
groff \  
less \  
libjpeg-turbo \  
libjpeg-turbo-dev \  
libpng \  
libpng-dev \  
libwebp \  
libwebp-dev \  
nasm \  
php7 \  
php7-bcmath \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-exif \  
php7-gd \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-mysqli \  
php7-opcache \  
php7-openssl \  
php7-pcntl \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-phar \  
php7-session \  
php7-simplexml \  
php7-soap \  
php7-tokenizer \  
php7-xdebug \  
php7-xml \  
php7-xmlreader \  
php7-xmlwriter \  
php7-zip \  
php7-zlib \  
py-pip \  
python \  
subversion \  
unzip \  
zip \  
zlib \  
zlib-dev  
  
# Boto - for AWS integration  
RUN pip --no-cache-dir install boto3  
  
# Composer with X-Debug  
RUN mkdir /composer  
  
WORKDIR /composer  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php --install-dir=/usr/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');" \  
&& composer require "drush/drush:~8.1.15" \--prefer-source --no-interaction \  
&& composer require "phpunit/phpunit:~6.4.3" \--prefer-source --no-interaction
\  
&& composer require "phpunit/php-invoker" \--prefer-source --no-interaction \  
&& ln -s /composer/vendor/bin/phpunit /usr/local/bin/phpunit \  
&& ln -s /composer/vendor/drush/drush/drush /usr/local/bin/drush \  
&& sed -i 's/\;z/z/g' /etc/php7/conf.d/xdebug.ini \  
&& php -m | grep -i xdebug  
  
WORKDIR /tmp  
  
# NPM from Edge (don't run any more apk add after this)  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/main >
/etc/apk/repositories  
RUN apk add --no-cache nodejs-npm  
  
# Bower and Gulp  
RUN npm install -g bower grunt-cli gulp-cli && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
  
# Get AWS CLI tools installed  
RUN pip --no-cache-dir install awscli  
  
VOLUME ["/app"]  
WORKDIR /app  
  
CMD ["/bin/sh"]

