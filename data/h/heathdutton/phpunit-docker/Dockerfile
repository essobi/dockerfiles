# PHPUnit Docker Container.  
FROM alpine:edge  
MAINTAINER Julien Breux <julien.breux@gmail.com>  
  
ENV PEAR_PACKAGES foo \  
GULP_VERSION 3.9.1 \  
BOWER_VERSION 1.8.0 \  
NPM_VERSION 3.7.1 \  
NODE_SASS_PLATFORM alpine  
  
WORKDIR /tmp  
  
RUN apk --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing add \  
bash \  
ca-certificates \  
git \  
curl \  
unzip \  
redis \  
php7 \  
php7-xml \  
php7-exif \  
php7-zip \  
php7-xmlreader \  
php7-zlib \  
php7-opcache \  
php7-mcrypt \  
php7-openssl \  
php7-curl \  
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
php7-simplexml \  
php7-xdebug \  
php7-pcntl \  
php7-ctype \  
php7-session \  
php7-tokenizer \  
php7-xmlwriter \  
php7-posix \  
php7-redis \  
&& php --version \  
&& php -r "copy('https://pear.php.net/go-pear.phar', 'go-pear.phar');" \  
&& php go-pear.phar \  
&& php -r "unlink('go-pear.phar');" \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php composer-setup.php --install-dir=/usr/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');" \  
&& composer require "phpunit/phpunit:~6.0.6" --prefer-source --no-interaction
\  
&& composer require "phpunit/php-invoker" --prefer-source --no-interaction \  
&& ln -s /tmp/vendor/bin/phpunit /usr/local/bin/phpunit \  
&& sed -i 's/nn and/nn, Julien Breux (Docker) and/g'
/tmp/vendor/phpunit/phpunit/src/Runner/Version.php  
# Enabling xdebug (currently nonfunctional due to alpine)  
# && sed -i 's/\;z/z/g' /etc/php7/conf.d/xdebug.ini \  
# && php -m | grep -i xdebug  
  
# Add dependencies for AWS EB deployments.  
RUN apk -v --update add \  
openssh \  
python \  
py-pip \  
&& pip install packaging==16.8 appdirs==1.4.0 awsebcli==3.7.8 --upgrade --user
\  
&& ln -s ~/.local/bin/eb /usr/local/bin/eb \  
&& apk -v --purge del py-pip \  
&& rm /var/cache/apk/*  
  
# Add all typical bower and gulp dependencies.  
RUN apk --no-cache add \  
nodejs \  
nodejs-npm \  
make \  
&& npm install --global --unsafe-perm "npm@latest" \  
&& npm install --global --unsafe-perm "bower@${BOWER_VERSION}" \  
&& npm install --global --unsafe-perm "gulp@${GULP_VERSION}" \  
&& npm install --global --unsafe-perm "node-sass@latest" \  
# Clean up  
&& rm -rf /root/.npm \  
&& find / -depth -type d -name test* -exec rm -rf {} \; \  
&& find / -depth -type f -name *.md -exec rm -f {} \; \  
&& find / -depth -type f -name *.yml -exec rm -f {} \;  
  
# Add rsync as commonly used in Bitbucket pipelines.  
RUN apk --no-cache add rsync  
  
ONBUILD RUN [ $PEAR_PACKAGES != "foo" ] && pear install $PEAR_PACKAGES  
  
VOLUME ["/app"]  
WORKDIR /app  
  
ENTRYPOINT ["/usr/local/bin/phpunit"]  
CMD ["--help"]  

