  
FROM arziel/php  
  
WORKDIR /var/docker  
  
# Add Composer's dependency's  
ADD composer.json /var/docker/composer.json  
RUN composer install --no-suggest --no-interaction  
  
## Add Slevomat Standard to PHPCS  
RUN ln -s /var/docker/vendor/slevomat/coding-standard/SlevomatCodingStandard
/var/docker/vendor/squizlabs/php_codesniffer/src/Standards/SlevomatCodingStandard  
  
# Add own standard  
ADD standard/ACS
/var/docker/vendor/squizlabs/php_codesniffer/src/Standards/ACS  
  
RUN echo "PHP Info"  
RUN php -v  
  
RUN echo "Installed Standards:"  
RUN /var/docker/vendor/bin/phpcs -i  
  
RUN echo "Slevomat Sniffs:"  
RUN /var/docker/vendor/bin/phpcs -se --standard=SlevomatCodingStandard  
  
RUN echo "Sniffs:"  
RUN /var/docker/vendor/bin/phpcs -se --standard=ACS  
  
WORKDIR /opt/project  
  
ENTRYPOINT ["php", "/var/docker/vendor/bin/phpcs", "--standard=ACS"]  

