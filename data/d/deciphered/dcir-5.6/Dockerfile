FROM drupalci/web-5.6  
# Update composer.  
RUN composer self-update  
  
# Install composer global packages.  
RUN composer global require decipher/dcir:0.5.0  
ENV PATH "$HOME/.composer/vendor/bin:$PATH"  
# Configure Code Sniffer for Drupal standards.  
RUN dcr install  
  
WORKDIR /var/www/html  
  
# Download and install Drupal 7.  
RUN drush dl drupal-7 --destination=/var/www/html --drupal-project-
rename=drupal-7 -y && \  
cd drupal-7 && \  
drush si --db-url=sqlite://sites/default/files/.ht.sqlite -y && \  
drush en simpletest -y  
  
# Patch Drupal 7 for simpletest/sqlite issue.  
RUN cd drupal-7 && \  
wget https://www.drupal.org/files/issues/1713332-76.patch && \  
patch -p1 < 1713332-76.patch  
  
# Download and install Drupal 8.  
RUN drush dl drupal-8 --destination=/var/www/html --drupal-project-
rename=drupal-8 -y && \  
cd drupal-8 && \  
drush si --db-url=sqlite://sites/default/files/.ht.sqlite -y && \  
drush en simpletest -y  
  
# Setup volume for project.  
VOLUME ["/dcir"]  
  
# Set DCIR as the entrypoint.  
ENTRYPOINT ["dcir"]

