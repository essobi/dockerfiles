FROM debian:jessie  
MAINTAINER Martin Helmich <m.helmich@mittwald.de>  
  
ENV COMPOSER_HOME=/usr/local/composer  
  
ADD https://getcomposer.org/composer.phar /usr/bin/composer  
RUN chmod +x /usr/bin/composer  
RUN apt-get update && apt-get install -y git  
RUN apt-get install -y php5-cli php5-xsl  
RUN composer global require --update-no-dev phpdocumentor/phpdocumentor
"~2.8.0"  
RUN ln -s ${COMPOSER_HOME}/vendor/bin/phpdoc /usr/bin/phpdoc  
  
WORKDIR /work  
ENTRYPOINT ["/usr/bin/php", "/usr/bin/phpdoc"]  

