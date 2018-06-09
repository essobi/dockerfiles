FROM php:7.2-cli-alpine3.7  
LABEL maintainer="Takamichi URATA <taka@seraphimis.net>"  
  
COPY script/docker-entrypoint.sh /usr/local/bin  
RUN mkdir -p /workdir; \  
chmod a+x /usr/local/bin/docker-entrypoint.sh; \  
apk add --no-cache su-exec  
  
VOLUME ["/workdir"]  
WORKDIR /workdir  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD []  
  
ENV PHPCS_VERSION 3.2.3  
RUN curl -sSL
https://github.com/squizlabs/PHP_CodeSniffer/releases/download/${PHPCS_VERSION}/phpcs.phar
\  
-o /usr/local/bin/phpcs; \  
chmod a+x /usr/local/bin/phpcs; \  
curl -sSL
https://github.com/squizlabs/PHP_CodeSniffer/releases/download/${PHPCS_VERSION}/phpcbf.phar
\  
-o /usr/local/bin/phpcbf; \  
chmod a+x /usr/local/bin/phpcbf; \  
phpcs --version  

