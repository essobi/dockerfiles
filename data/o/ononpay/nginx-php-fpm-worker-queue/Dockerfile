FROM ononpay/nginx-php-fpm:latest  
  
MAINTAINER Duong Dinh Cuong <dinhcuong@ononpay.com>  
  
ENV ERRORS "YES"  
ENV SKIP_CHOWN "YES"  
ENV SKIP_COMPOSER ""  
ENV APPLICATION_ENV "production"  
COPY ./conf.d /etc/supervisor/conf.d  
  
# Download and build beanstalk  
ENV VERSION_BEANSTALKD="1.10"  
RUN addgroup -S beanstalkd && adduser -S -G beanstalkd beanstalkd  
RUN apk add --no-cache 'su-exec>=0.2'  
RUN apk add --update --no-cache --virtual build-dependencies freetype-dev
libpng-dev libjpeg-turbo-dev libxml2-dev gcc make musl-dev curl \  
&& curl -sL
https://github.com/kr/beanstalkd/archive/v$VERSION_BEANSTALKD.tar.gz | tar xvz
-C /tmp \  
&& cd /tmp/beanstalkd-$VERSION_BEANSTALKD \  
&& sed -i "s|#include <sys/fcntl.h>|#include <fcntl.h>|g" sd-daemon.c \  
&& make \  
&& cp beanstalkd /usr/bin \  
&& apk del build-dependencies \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  
# Post installation packages without clearing cache and dependancies  
RUN apk add --update --no-cache gcc make autoconf g++ libtool pcre-dev wget
imagemagick-dev \  
&& cd /tmp \  
&& wget https://pecl.php.net/get/imagick-3.4.3.tgz \  
&& tar xvzf imagick-3.4.3.tgz \  
&& cd imagick-3.4.3 \  
&& phpize \  
&& ./configure \  
&& make install \  
&& rm -rf /tmp/imagick-3.4.3 \  
&& echo extension=imagick.so >> /usr/local/etc/php/conf.d/imagick.ini  
  
WORKDIR $PROJECTROOT  
  
EXPOSE 443 80  
CMD ["/entrypoint.sh"]

