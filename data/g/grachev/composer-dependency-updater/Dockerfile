FROM composer:1.6.2  
LABEL MAINTAINER="Konstantin Grachev <me@grachevko.ru>"  
  
ENV APP_DIR=/usr/local/app \  
COMPOSER_CACHE_DIR=/var/cache/composer  
  
ENV PATH=${APP_DIR}/bin:${APP_DIR}/vendor/bin:${PATH}  
  
WORKDIR ${APP_DIR}  
  
RUN composer global require "hirak/prestissimo:^0.3"  
  
COPY . ./  
  
RUN composer install --no-scripts --no-interaction --apcu-autoloader --no-
progress --prefer-dist \  
&& rm -rf ${COMPOSER_CACHE_DIR}/*  
  
ENTRYPOINT ["cdu"]  

