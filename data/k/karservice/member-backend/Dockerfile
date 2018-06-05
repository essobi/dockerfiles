FROM alpine:3.6  
ENV APP_DEBUG=true \  
APP_ROOT=/app \  
APP_URL=https://api.medlem.karservice.se  
RUN mkdir -p ${APP_ROOT}  
WORKDIR ${APP_ROOT}  
EXPOSE 80  
COPY apk-packages.txt ${APP_ROOT}/  
RUN apk add --no-cache $(grep -vE "^\s*#" ${APP_ROOT}/apk-packages.txt | tr
"\r\n" " ") && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
COPY package.json yarn.lock ${APP_ROOT}/  
RUN yarn install && yarn cache clean  
  
COPY . ${APP_ROOT}/  
RUN composer install --no-interaction && \  
mkdir -p /run/apache2 && \  
ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log && \  
ln -sf ${APP_ROOT}/apache-site.conf /etc/apache2/conf.d/app.conf && \  
chown -R apache:apache ${APP_ROOT}  
  
CMD ["httpd", "-DFOREGROUND"]  

