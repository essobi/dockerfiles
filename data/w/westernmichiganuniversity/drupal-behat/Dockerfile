# Western Michigan University's image for testing a Drupal site with Behat.  
FROM westernmichiganuniversity/drupal-environment:latest  
  
# Install prerequisites.  
RUN apk --no-cache add \  
dbus \  
firefox-esr \  
openjdk7-jre-base \  
rsync \  
ttf-freefont \  
xvfb  
RUN dbus-uuidgen --ensure=/etc/machine-id  
  
# Install Selenium to support JavaScript-enabled Behat tests.  
RUN wget "http://selenium-release.storage.googleapis.com/2.53/selenium-server-
standalone-2.53.0.jar" -O /usr/local/bin/selenium-server-standalone.jar  
  
# Create a mount point for the Drupal project.  
RUN mkdir -p /opt/project  
ENV PROJECT /opt/project  
VOLUME ${PROJECT}  
  
# Default path to the project's Drupal root directory.  
ENV DRUPAL_ROOT ${PROJECT}/web  
  
# Default install profile for the Drupal site.  
ENV PROFILE minimal  
  
# Expected location of the Drush executable.  
ENV DRUSH ${PROJECT}/vendor/bin/drush  
  
# Copy in our entrypoint script.  
COPY bin/docker-drupal-behat-* /usr/local/bin/  
  
WORKDIR /var/www/html  
ENTRYPOINT ["docker-drupal-behat-entrypoint.sh"]  
# Pass the Behat executable (relative to $PROJECT) as the entrypoint argument.  
CMD ["vendor/bin/behat", "--no-interaction", "--format=junit", "--
format=pretty"]  

