FROM shito/alpine-php7-cli:edge  
MAINTAINER Sebastian Knoth <sk@bytepark.de>  
  
WORKDIR /tmp  
  
# Add CURL and required php7 extensions  
RUN apk upgrade -U && \  
apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing add
\  
curl \  
php7-phar  
  
# Install composer global bin  
RUN curl -sSL https://phar.phpunit.de/phpunit.phar -o phpunit.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit  
  
RUN apk del curl && \  
rm -fr /var/cache/apk/*  
  
WORKDIR /usr/share/nginx/html  
  
ENTRYPOINT ["phpunit"]

