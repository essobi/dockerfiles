FROM alpine as confd  
  
ENV GOPATH /go  
  
RUN mkdir -p "$GOPATH/src/" "$GOPATH/bin" && chmod -R 777 "$GOPATH" && \  
mkdir -p /go/src/github.com/kelseyhightower/confd  
  
RUN apk --update add unzip curl go bash git libc-dev && \  
ln -s /go/src/github.com/kelseyhightower/confd /app  
  
WORKDIR /app  
  
RUN curl -L https://github.com/kelseyhightower/confd/archive/v0.13.0.zip
--output /tmp/confd.zip && \  
unzip -d /tmp/confd /tmp/confd.zip && \  
cp -r /tmp/confd/*/* /app && \  
rm -rf /tmp/confd* && \  
./build  
  
FROM composer  
  
FROM php:7-alpine  
  
COPY \--from=composer /usr/bin/composer /usr/local/bin/composer  
  
COPY \--from=confd /app/bin/confd /usr/local/bin/confd  
  
# Set Python versions  
ENV PYTHON_VERSION=2.7.12-r0  
ENV PY_PIP_VERSION=8.1.2-r0  
ENV SUPERVISOR_VERSION=3.3.1  
RUN apk add --no-cache --virtual .ext-deps \  
unzip \  
curl \  
vim \  
bash \  
git \  
libpng-dev \  
libjpeg-turbo-dev \  
freetype-dev \  
libwebp-dev \  
mariadb-client \  
python=$PYTHON_VERSION \  
py-pip=$PY_PIP_VERSION  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ --with-png-dir=/usr/include --with-webp-dir=/usr/include  
  
RUN pecl install xdebug && \  
pecl clear-cache  
  
RUN docker-php-ext-install mysqli pdo_mysql zip bcmath gd && \  
docker-php-ext-enable xdebug && \  
docker-php-source delete  
  
RUN pip install supervisor==$SUPERVISOR_VERSION  
  
RUN mkdir /var/log/supervisor  
  
# Set the Drush version.  
ENV DRUSH_VERSION 8.1.13  
# Install Drush using Composer.  
RUN composer global require drush/drush:"$DRUSH_VERSION" \--prefer-dist  
  
# Set the Drupal Console version.  
ENV DRUPAL_CONSOLE_VERSION "dev-master"  
# Install Drupal Console using Composer.  
RUN composer global require drupal/console:"$DRUPAL_CONSOLE_VERSION"
\--prefer-dist  
  
ADD supervisord.conf /etc/  
ADD confd /etc/confd  
ADD scripts /root/  
ADD supervisord-services.conf /etc/supervisor/conf.d/services.conf  
  
WORKDIR /var/www/site  
ENV PATH="/root/.composer/vendor/bin:${PATH}"  
VOLUME /var/www/site  
  
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration",
"/etc/supervisord.conf"]  

