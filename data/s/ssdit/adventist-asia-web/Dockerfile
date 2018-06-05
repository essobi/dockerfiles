FROM ssdit/adventist-asia-web-base:latest  
  
ARG BUILD_ASSETS  
  
COPY php.ini /usr/local/etc/php/  
COPY . /var/www/html  
WORKDIR /var/www/html  
RUN mkdir /var/www/html/site/assets/sessions \  
/var/www/html/site/assets/logs \  
/var/www/html/site/assets/files \  
/var/www/html/site/assets/cache \  
&& chown -R www-data:www-data * \  
&& chmod -R o+x *  
  
# build assets  
RUN yarn install && yarn build;  
RUN set -ex; \  
if [ -n "$BUILD_ASSETS" ]; then \  
yarn install && yarn build; \  
fi;  

