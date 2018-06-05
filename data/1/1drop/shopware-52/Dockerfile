#++++++++++++++++++++++++++++++++++++++  
# PHP application Docker container  
#++++++++++++++++++++++++++++++++++++++  
FROM webdevops/php-nginx:ubuntu-16.04  
ENV PROVISION_CONTEXT "production"  
# Deploy scripts/configurations  
COPY etc/ /opt/docker/etc/  
# This is necessary otherwise the shopware nginx conf conflicts with the
existing one  
RUN rm /opt/docker/etc/nginx/vhost.common.d/10-location-root.conf  
COPY provision/ /opt/docker/provision/  
  
RUN /opt/docker/bin/provision add --tag bootstrap --tag entrypoint
boilerplate-main boilerplate-main-development \  
&& /opt/docker/bin/bootstrap.sh  
  
RUN /usr/local/bin/apt-install ant  
  
# Install PHP-CodeSniffer  
RUN curl -o /usr/local/bin/phpcs -L
https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \  
&& chmod +x /usr/local/bin/phpcs  
  
# Install PHPUnit  
RUN curl -o /usr/local/bin/phpunit -L https://phar.phpunit.de/phpunit.phar \  
&& chmod +x /usr/local/bin/phpunit  
  
# Configure volume/workdir  
RUN mkdir -p /app/  
WORKDIR /app/  
RUN git clone \--depth 1 -b "v5.2.20" https://github.com/shopware/shopware.git
/app/ \  
&& echo "5.2.20" > recovery/install/data/version \  
&& sed -i 's/\\_\\_\\_VERSION\\_\\_\\_/5.2.20/g'
engine/Shopware/Application.php \  
&& sed -i 's/\\_\\_\\_VERSION\\_TEXT\\_\\_\\_//g'
engine/Shopware/Application.php \  
&& sed -i "s/\\_\\_\\_REVISION\\_\\_\\_/$(git rev-parse --short HEAD)/g"
engine/Shopware/Application.php \  
&& composer install  
RUN chown -R application:application /app/  

