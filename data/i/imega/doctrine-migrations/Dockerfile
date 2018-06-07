FROM alpine:3.4  
MAINTAINER Dmitry Gavriloff <info@imega.ru>  
  
RUN apk --update add curl php5 php5-mysql php5-json php5-zlib php5-phar
php5-pdo_mysql && \  
curl -sS -0L
https://github.com/doctrine/migrations/releases/download/1.4.1/doctrine-
migrations.phar -o /usr/bin/doctrine-migrations && \  
chmod +x /usr/bin/doctrine-migrations && \  
apk del curl && \  
rm -rf /var/cache/apk/*  
  
VOLUME ["/data"]  
  
ENTRYPOINT ["doctrine-migrations"]  

