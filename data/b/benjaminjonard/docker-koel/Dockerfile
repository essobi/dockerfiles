FROM alpine:edge  
  
LABEL maintainer="Benjamin Jonard <jonard.benjamin@gmail.com>"  
  
ENV UID=991 GID=991  
ENV DB_HOST ""  
ENV DB_DATABASE ""  
ENV DB_USERNAME ""  
ENV DB_PASSWORD ""  
ENV APP_URL ""  
ENV ADMIN_EMAIL ""  
ENV ADMIN_NAME ""  
ENV ADMIN_PASSWORD ""  
ENV APP_DEBUG false  
ENV AP_ENV production  
  
RUN apk update \  
&& apk upgrade --update-cache --available \  
&& apk add \  
curl \  
bash \  
less \  
vim \  
nginx \  
ca-certificates \  
nodejs \  
nodejs-npm \  
php7 \  
php7-fpm \  
php7-mbstring \  
php7-simplexml \  
php7-json \  
php7-zlib \  
php7-xml \  
php7-session \  
php7-pdo \  
php7-phar \  
php7-openssl \  
php7-pdo_mysql \  
php7-mysqli \  
php7-gd \  
php7-iconv \  
php7-mcrypt \  
php7-curl \  
php7-opcache \  
php7-ctype \  
php7-apcu \  
php7-intl \  
php7-bcmath \  
php7-dom \  
php7-xmlreader \  
php7-xmlwriter \  
php7-xsl \  
php7-zip \  
php7-tokenizer \  
mysql-client \  
git \  
build-base \  
python \  
s6 \  
su-exec \  
&& apk add -u musl \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer --version  
  
RUN mkdir /koel \  
&& last_tag=$(curl -sX GET
"https://api.github.com/repos/phanan/koel/releases/latest" | awk
'/tag_name/{print $4;exit}' FS='[""]') \  
&& curl -o /tmp/koel.tar.gz -L
"https://github.com/phanan/koel/archive/${last_tag}.tar.gz" \  
&& tar xf /tmp/koel.tar.gz -C /koel --strip-components=1 \  
&& rm -rf /tmp/* \  
&& cd /koel \  
&& npm install yarn -g \  
&& composer install -o --no-scripts --no-progress --no-suggest \  
&& composer clear-cache \  
&& touch .env  
  
RUN cd /koel && yarn install  
RUN cd /koel && key=$(php artisan key:generate --show) && echo
"APP_KEY=${key}" >> .env && php artisan koel:generate-jwt-secret  
  
#clean up  
RUN apk del --purge git build-base python curl  
  
COPY ./nginx.conf /etc/nginx/nginx.conf  
COPY ./php.ini /usr/local/etc/php/php.ini  
COPY php-fpm.conf /etc/php7/php-fpm.conf  
COPY s6.d /etc/s6.d  
COPY run.sh /usr/local/bin/run.sh  
  
RUN chmod +x /usr/local/bin/run.sh /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*  
  
WORKDIR "/koel"  
  
EXPOSE 8870  
VOLUME ["/koel/music"]  
  
CMD ["run.sh"]  

