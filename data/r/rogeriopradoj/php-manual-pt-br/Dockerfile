FROM rogeriopradoj/php-manual-pt-br-repositories  
  
MAINTAINER rogeriopradoj <rogeriopradoj@gmail.com>  
  
COPY .scripts/ /scripts  
  
WORKDIR /php-manual-pt-br  
  
VOLUME /php-manual-pt-br  
  
ENTRYPOINT ["/scripts/0-default.sh"]  
  
CMD ["php -S 0.0.0.0:4000 -t /php-manual-pt-br/web-php"]

