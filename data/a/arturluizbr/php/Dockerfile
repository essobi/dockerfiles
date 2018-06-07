FROM alpine:3.3  
MAINTAINER Artur Oliveira <artur@arturluiz.com.br>  
  
ENV PHP_VERSION 5.6.0  
ENV MAKE_JOBS 28  
# Alpine repository provides bison 3.0 that is incompatible with PHP/Zend 5.6,
if you find any problem open an issue  
RUN apk -U add wget autoconf automake libtool re2c flex bison g++ make
libxml2-dev \  
&& wget -q --no-check-certificate https://github.com/php/php-
src/archive/php-${PHP_VERSION}.zip \  
&& unzip -q php-${PHP_VERSION}.zip \  
&& mv php-src-php-${PHP_VERSION} php-${PHP_VERSION}-src \  
&& cd php-${PHP_VERSION}-src \  
&& ./genfiles \  
&& ./buildconf --force --copy \  
&& ./configure \  
&& make -j$MAKE_JOBS \  
&& make -j$MAKE_JOBS install \  
&& apk del wget autoconf automake libtool re2c flex bison g++ make libxml2-dev
\  
&& apk add libxml2 \  
&& rm /php-${PHP_VERSION}.zip \  
&& rm -rf /php-${PHP_VERSION}-src  
  
WORKDIR /app  
  
EXPOSE 80  
CMD ["php", "-S", "0.0.0.0:80"]

