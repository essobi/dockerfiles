FROM php:5.6-alpine  
  
CMD [ "/bin/sh" ]  
  
RUN apk add --no-cache curl  
  
ENV COMPOSER_VERSION="1.4.2"  
RUN curl -L https://getcomposer.org/installer \  
| php -- --install-dir /usr/local/bin --filename composer --version
${COMPOSER_VERSION}  
  
ENV PHP_PARALLEL_LINT_VERSION="0.9.2"  
RUN COMPOSER_HOME=/usr/local/share/composer COMPOSER_BIN_DIR=/usr/local/bin
composer global require \  
jakub-onderka/php-parallel-lint:${PHP_PARALLEL_LINT_VERSION} jakub-
onderka/php-console-highlighter && \  
rm -rf /root/.composer  

