FROM php:7.0-cli  
  
ENV EXT_MONGO_VERSION 1.3.2  
ENV EXT_XDEBUG_VERSION 2_5_5  
ENV EXT_YAC_VERSION 2.0.2  
COPY ./config/sources.list /etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN apt-get update && apt-get install -y libcurl4-openssl-dev \  
&& docker-php-ext-install -j$(nproc) curl  
  
RUN apt-get update && apt-get install -y libicu-dev \  
&& docker-php-ext-install -j$(nproc) intl  
  
RUN apt-get update && docker-php-ext-install -j$(nproc) \  
bcmath hash json mbstring ctype \  
mysqli pdo pdo_mysql \  
session sockets  
  
RUN apt-get update && docker-php-ext-install -j$(nproc) \  
calendar \  
fileinfo \  
gettext \  
posix  
  
RUN cd /tmp && curl -SL
"https://github.com/xdebug/xdebug/archive/XDEBUG_${EXT_XDEBUG_VERSION}.tar.gz"
| tar xzf - && cd xdebug-XDEBUG_${EXT_XDEBUG_VERSION} \  
&& phpize && ./configure --enable-xdebug && make -j$(nproc) && make install  
COPY ./config/xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  
  
RUN apt-get update && apt-get install -y libssl-dev \  
&& cd /tmp && curl -SL "https://github.com/mongodb/mongo-php-
driver/releases/download/${EXT_MONGO_VERSION}/mongodb-${EXT_MONGO_VERSION}.tgz"
| tar xzf - && cd mongodb-${EXT_MONGO_VERSION} \  
&& phpize && ./configure --enable-mongodb && make -j$(nproc) && make install \  
&& docker-php-ext-enable mongodb  
  
RUN cd /tmp && curl -SL
"https://github.com/laruence/yac/archive/yac-${EXT_YAC_VERSION}.tar.gz" | tar
xzf - && cd yac-yac-${EXT_YAC_VERSION} \  
&& phpize && ./configure --enable-yac && make -j$(nproc) && make install \  
&& docker-php-ext-enable yac  
  
RUN docker-php-ext-install -j$(nproc) zip  
  
VOLUME /srv/http  
  
WORKDIR /srv/http  
  
RUN rm -rf /tmp/*  
  
# see https://stackoverflow.com/a/41648500/5968225  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  

