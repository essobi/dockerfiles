#++++++++++++++++++++++++++++++++++++++  
# PHP application Docker container  
#++++++++++++++++++++++++++++++++++++++  
FROM webdevops/php-apache-dev:centos-7  
ENV PROVISION_CONTEXT "development"  
ENV SHOPWARE_ENV "development"  
ENV WEB_DOCUMENT_ROOT "/app/"  
ENV WEB_DOCUMENT_INDEX "index.php"  
ENV CLI_SCRIPT "/app/n98-magerun.phar"  
ENV WEB_NO_CACHE_PATTERN "\\.(css|js|gif|png|jpg|svg)$"  
# Deploy scripts/configurations  
COPY etc/ /opt/docker/etc/  
COPY provision/ /opt/docker/bin/  
  
RUN mv /opt/docker/etc/php/development.ini /opt/docker/etc/php/php.ini  
  
# Add magento  
ADD https://github.com/OpenMage/magento-mirror/archive/1.9.3.0.tar.gz
/tmp/magento-ce-1.9.3.0.tar.gz  
RUN tar xzvf /tmp/magento-ce-1.9.3.0.tar.gz -C /tmp/ \  
&& rm -rf /app \  
&& mv /tmp/magento-mirror-1.9.3.0/ /app \  
&& rm /tmp/magento-ce-1.9.3.0.tar.gz \  
&& chmod +x /app/cron.sh  
  
# Install n98 mage-run  
ADD https://files.magerun.net/n98-magerun.phar /app/n98-magerun.phar  
RUN chmod +x /app/n98-magerun.phar  
  
# Must explicitly turned on in dev env (default off)  
RUN docker-service-enable cron  
  
# Install PHP-CodeSniffer  
RUN curl -o /usr/local/bin/phpcs -L
https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \  
&& chmod +x /usr/local/bin/phpcs  
  
# Install PHPUnit  
RUN curl -o /usr/local/bin/phpunit -L https://phar.phpunit.de/phpunit.phar \  
&& chmod +x /usr/local/bin/phpunit  
  
# END - DEV ONLY  
# Configure volume/workdir  
RUN chown -R application:application /app/  
WORKDIR /app/  

