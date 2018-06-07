# PHPCS Docker container  
# Docker Container for running PHPCS  
# Take a look at https://github.com/squizlabs/PHP_CodeSniffer  
FROM php:7.0-alpine  
RUN pear install PHP_CodeSniffer  
WORKDIR /app  
ENTRYPOINT [ "phpcs" ]  
CMD [ "--standard=PSR2", "/app" ]  

