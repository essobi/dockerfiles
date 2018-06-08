FROM shito/alpine-php7-cli:edge  
MAINTAINER Sebastian Knoth <sk@bytepark.de>  
  
WORKDIR /tmp  
  
# Add CURL and required php7 extensions  
RUN apk upgrade -U && \  
apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing add
\  
curl \  
php7-json \  
php7-phar \  
php7-openssl \  
php7-mbstring \  
php7-iconv \  
php7-dom  
  
# Install composer global bin  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer self-update  
  
RUN rm -fr /var/cache/apk/*  
  
WORKDIR /usr/share/nginx/html  
  
ENTRYPOINT ["composer"]  
CMD ["--help"]

