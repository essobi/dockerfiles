FROM php:7.1.5-alpine  
  
LABEL maintainer "itiQiti SAS <opensource@itiqiti.com>"  
LABEL creator "Mikael Robert <mikaelrob@gmail.com>"  
  
ENV MODE=default \  
CHOWN_DIRS= \  
PHP_PHP_ADMIN_DATE_TIMEZONE=Europe/Paris \  
PHP_FILE= \  
PHP_CODE=  
  
RUN apk add --update --no-cache --virtual .build-deps curl && \  
curl -s -f -L https://github.com/itiqiti/dkconf/releases/download/0.2/dkconf-
linux -o /usr/local/bin/dkconf && \  
chmod +x /usr/local/bin/dkconf && \  
apk del .build-deps  
  
COPY ["templates", "/usr/local/etc/php/conf.d/templates"]  
COPY ["default.sh", "/usr/local/bin/php-default-exec-file.sh"]  
COPY ["docker-entrypoint.sh", "/usr/local/bin/"]  
  
WORKDIR /app/  
  
CMD ["/usr/local/bin/docker-entrypoint.sh"]  

