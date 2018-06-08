FROM composer  
  
ENV PATH "/tmp/vendor/bin:$PATH"  
ENV COMPOSER_HOME /tmp  
  
ENV PACKAGE friendsofphp/php-cs-fixer  
  
RUN composer global require ${PACKAGE} \  
&& composer clear-cache  
  
CMD ["php-cs-fixer"]

