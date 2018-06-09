# Drush Docker Container  
FROM tomsowerby/php-5.3-composer  
  
MAINTAINER Mads H. Danquah <mads@danquah.dk>  
  
# Drush 6 needs the Console_Table pear.  
RUN pear install Console_Table  
  
# Install Drush using Composer  
RUN composer global require drush/drush:"6.*" \--prefer-dist  
  
# Setup the symlink  
RUN ln -sf $COMPOSER_HOME/vendor/bin/drush.php /usr/local/bin/drush  
  
RUN apt-get update && apt-get install -y mysql-client libmysqlclient-dev  
RUN docker-php-ext-install mysql  
RUN docker-php-ext-install mysqli  
RUN docker-php-ext-install pdo_mysql  
  
# Display which version of Drush was installed  
RUN drush --version  
  
# Update the entry point of the application  
ENTRYPOINT ["drush"]

