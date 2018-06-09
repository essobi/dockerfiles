#FROM php:7.1.1-alpine  
FROM php:5.6.30-alpine  
  
# Install dependencies  
RUN apk --update-cache --verbose add curl wget sudo bash git openssh && \  
rm -rf /var/cache/apk/* && \  
curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer && \  
wget https://github.com/clue/phar-composer/releases/download/v1.0.0/phar-
composer.phar && chmod 755 phar-composer.phar && mv phar-composer.phar
/usr/local/bin/phar-composer && \  
mkdir /app && \  
adduser -D -u 1000 composer  
  
ENV COMPOSER=composer.json  
  
VOLUME ["/app"]  
  
WORKDIR /app  
  
# Add the entrypoint  
ADD entrypoint.sh /usr/local/bin/  
  
# Auto-login with the composer user  
USER composer  
  
# Determine Entrypoint  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["help"]  

