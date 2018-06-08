# Western Michigan University's image for testing a Drupal module with Behat.  
FROM westernmichiganuniversity/drupal-behat:latest  
  
# Name of the subdirectory of the project that contains its Composer-managed
dependencies.  
ENV VENDOR vendor  
  
# Default paths to the directories containing Drupal Core, modules, etc.  
ENV DRUPAL_CORE ${PROJECT}/${VENDOR}/drupal/drupal  
ENV DRUPAL_MODULES ${PROJECT}/${VENDOR}/drupal/modules  
ENV DRUPAL_LIBRARIES ${PROJECT}/${VENDOR}/drupal/libraries  
  
# Copy in our entrypoint script.  
COPY bin/docker-drupal-module-behat-* /usr/local/bin/  
  
WORKDIR /var/www/html  
ENTRYPOINT ["docker-drupal-module-behat-entrypoint.sh"]  
# Pass the Behat executable (relative to $PROJECT) as the entrypoint argument.  
CMD ["vendor/bin/behat", "--no-interaction", "--format=junit", "--
format=pretty"]  

