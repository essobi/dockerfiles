FROM php:7.1-alpine  
  
ENV COMPOSER_HOME=/composer \  
COMPOSER_ALLOW_SUPERUSER=1 \  
PATH=/composer/vendor/bin:$PATH  
  
ARG CODER_VERSION=8.2.12  
RUN set -xe \  
&& apk add --no-cache --virtual .build-deps \  
git \  
curl \  
&& curl -sSL https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer \  
&& composer global require drupal/coder:"${CODER_VERSION}" \  
&& phpcs --config-set installed_paths
"${COMPOSER_HOME}/vendor/drupal/coder/coder_sniffer" \  
&& apk del .build-deps  
  
COPY php/ /usr/local/etc/php/conf.d/  
  
WORKDIR /workspace  
  
CMD ["phpcs", "--standard=Drupal", "--ignore=node_modules,*.css,*.md,*.txt",
"/workspace"]  

