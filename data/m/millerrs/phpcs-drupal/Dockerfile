FROM alpine:3.7  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /composer  
ENV PATH /composer/vendor/bin:$PATH  
  
RUN apk add --no-cache \  
curl \  
git \  
php7 \  
php7-ctype \  
php7-iconv \  
php7-json \  
php7-mbstring \  
php7-openssl \  
php7-phar \  
php7-simplexml \  
php7-tokenizer \  
php7-xml \  
php7-xmlwriter \  
php7-zlib \  
&& curl --silent --show-error https://getcomposer.org/installer | php \  
&& php composer.phar global require drupal/coder \  
&& phpcs --config-set installed_paths
/composer/vendor/drupal/coder/coder_sniffer  
  
WORKDIR /app  
  
CMD ["phpcs", "--standard=Drupal,DrupalPractice", "."]

