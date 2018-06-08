FROM spacedgap/centos:6-remi-php5.6  
# Start as root  
USER root  
  
# Install Libraries and Packages  
RUN yum -y install \  
## PHP Libraries  
php-cli \  
php-common \  
php-pear \  
php-mbstring \  
php-mysqlnd \  
php-pdo \  
php-pecl-jsonc \  
php-pecl-zip \  
php-process \  
php-xml  
  
RUN pecl update-channels  
  
# Clean up  
RUN yum clean all && \  
rm -rf \  
/var/cache/* \  
/tmp/* \  
/var/tmp/*  
  
COPY ./scripts/entrypoint/docker-php-entrypoint /usr/local/bin/  
  
RUN chmod 755 /usr/local/bin/docker-php-entrypoint  
  
ENTRYPOINT ["/usr/bin/tini", "--", "docker-php-entrypoint"]  
  
CMD ["php", "-a"]  

