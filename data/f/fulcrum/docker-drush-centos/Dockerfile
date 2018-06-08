FROM fulcrum/php  
MAINTAINER IF Fulcrum "fulcrum@ifsight.net"  
  
ENV COLUMNS=256  
# Enable EPEL Repos, update, install PHP 5.6, install composer & drush  
RUN rpm --rebuilddb && \  
yum --noplugins install -y git which mysql && \  
yum --noplugins upgrade -y && \  
package-cleanup --dupes && \  
package-cleanup --cleandupes && \  
yum clean all && \  
cd /usr/local && \  
curl -sS https://getcomposer.org/installer | php && \  
/bin/mv composer.phar bin/composer && \  
chsh -s /bin/bash php && \  
usermod -d /tmp/phphome php && \  
mkdir -p /usr/share/drush/commands/ /tmp/phphome drush7 drush8 && \  
chown php.php /tmp/phphome drush7 drush8 && \  
su - php -c "cd /usr/local/drush7 && composer require drush/drush:7.*" && \  
su - php -c "cd /usr/local/drush8 && composer require drush/drush:8.*" && \  
ln -s /usr/local/drush7/vendor/drush/drush/drush /usr/local/bin/drush && \  
ln -s /usr/local/drush7/vendor/drush/drush/drush /usr/local/bin/drush7 && \  
ln -s /usr/local/drush8/vendor/drush/drush/drush /usr/local/bin/drush8 && \  
su - php -c "/usr/local/bin/drush @none dl registry_rebuild" && \  
mv /tmp/phphome/.drush/registry_rebuild /usr/share/drush/commands/ && \  
usermod -d /var/www/html php  
  
USER php  
  
# Move to the directory were the php files stands  
WORKDIR /var/www/html  
  
ENTRYPOINT ["/usr/local/bin/drush"]  

