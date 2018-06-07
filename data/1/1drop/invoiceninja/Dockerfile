FROM webdevops/php-nginx:debian-9  
ENV WEB_DOCUMENT_ROOT /app/public/  
ENV WEB_DOCUMENT_INDEX index.php  
ENV PROVISION_CONTEXT production  
ENV APP_ENV production  
ENV APP_DEBUG 0  
ENV APP_KEY SomeRandomString  
ENV LOG errorlog  
ENV APP_CIPHER AES-256-CBC  
ENV SELF_UPDATER_SOURCE ''  
ENV PHANTOMJS_BIN_PATH /usr/bin/phantomjs  
ENV PHP_OPCACHE_REVALIDATE_FREQ 60  
ENV php.opcache.enable_cli 1  
RUN apt-install php7.0-gmp phantomjs  
  
#####  
# DOWNLOAD AND INSTALL INVOICE NINJA  
#####  
ENV INVOICENINJA_VERSION 4.2.0  
RUN composer self-update \  
&& curl -o invoiceninja.tar.gz -SL
https://github.com/invoiceninja/invoiceninja/archive/v${INVOICENINJA_VERSION}.tar.gz
\  
&& tar -xzf invoiceninja.tar.gz -C /tmp/ \  
&& rm invoiceninja.tar.gz \  
&& mv /tmp/invoiceninja-${INVOICENINJA_VERSION} /tmp/app \  
&& mv /tmp/app / \  
&& composer install -d /app -o --no-dev --no-interaction --no-progress \  
&& chown -R ${APPLICATION_UID}:${APPLICATION_GID} /app \  
&& rm -rf /app/app/docs /app/app/tests  

