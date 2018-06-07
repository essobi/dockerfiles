FROM alpine:edge  
  
LABEL maintainer="Benjamin Jonard <jonard.benjamin@gmail.com>"  
  
ENV APP_ENV "prod"  
ENV APP_DEBUG 0  
ENV APP_SECRET "937lZdyx5gfBwPpQZ074"  
ENV DATABASE_URL ""  
ENV SHOW_ADMIN_TOOLS 0  
COPY composer.json /ppm/composer.json  
COPY run.sh /etc/app/run.sh  
COPY php.ini /etc/php7/php.ini  
COPY nginx.conf /etc/nginx/nginx.conf  
  
#Install dependencies  
RUN BUILD_DEPS=" \  
tar \  
libressl \  
ca-certificates \  
build-base \  
autoconf \  
pcre-dev \  
libtool" \  
&& apk update \  
&& apk upgrade --update-cache --available \  
&& apk add \  
${BUILD_DEPS} \  
bash \  
git \  
unzip \  
nginx \  
curl \  
php7 \  
php7-cgi \  
php7-dom \  
php7-xml \  
php7-xmlwriter \  
php7-curl \  
php7-mbstring \  
php7-fpm \  
php7-exif \  
php7-openssl \  
php7-gd \  
php7-phar \  
php7-json \  
php7-pdo \  
php7-pdo_pgsql \  
php7-zip \  
php7-session \  
php7-ctype \  
php7-apcu \  
php7-tokenizer \  
php7-opcache \  
php7-simplexml \  
php7-fileinfo \  
php7-sodium \  
php7-iconv \  
php7-intl \  
php7-pcntl \  
&& apk del ${BUILD_DEPS} \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
#Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer --version \  
#Install ppm  
&& cd /ppm \  
&& composer install -o \  
#Create project directory  
&& mkdir -p /koillection \  
&& last_tag=$(curl -sX GET
"https://api.github.com/repos/koillection/koillection/releases/latest" | awk
'/tag_name/{print $4;exit}' FS='[""]') \  
&& curl -o /tmp/koillection.tar.gz -L
"https://github.com/koillection/koillection/archive/${last_tag}.tar.gz" \  
&& tar xf /tmp/koillection.tar.gz -C /koillection --strip-components=1 \  
&& rm -rf /tmp/* \  
&& cd /koillection \  
&& touch .env \  
&& composer install -o --no-scripts --no-progress --no-suggest \  
&& composer clear-cache \  
&& mkdir -p /run/nginx  
  
EXPOSE 80  
WORKDIR "/koillection"  
  
VOLUME ["/koillection/public/uploads"]  
  
ENTRYPOINT ["/bin/bash", "/etc/app/run.sh"]  
  

