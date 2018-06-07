FROM php:5.6.30-fpm-alpine  
  
LABEL maintainer "itiQiti SAS <opensource@itiqiti.com>"  
LABEL creator "Mikael Robert <mikaelrob@gmail.com>"  
  
ENV MODE=default \  
FPM_CHOWN_DIRS= \  
FPM_PHP_ADMIN_DATE_TIMEZONE=Europe/Paris \  
FPM_FPM_USER=www-data \  
FPM_FPM_GROUP=www-data  
  
RUN apk add --update --no-cache --virtual .build-deps curl && \  
curl -s -f -L https://github.com/itiqiti/dkconf/releases/download/0.2/dkconf-
linux -o /usr/local/bin/dkconf && \  
chmod +x /usr/local/bin/dkconf && \  
apk del .build-deps && \  
rm -f /usr/local/etc/php-fpm.d/*.conf  
  
COPY ["templates", "/usr/local/etc/php-fpm.d/templates"]  
COPY ["docker-entrypoint.sh", "/usr/local/bin/"]  
  
WORKDIR /app/  
  
CMD ["/usr/local/bin/docker-entrypoint.sh"]  

