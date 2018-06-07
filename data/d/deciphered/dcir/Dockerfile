FROM drupalci/web-5.6  
WORKDIR /var/www/html  
  
# Update composer.  
RUN composer self-update  
  
# Install composer global packages.  
COPY ./composer.json /root/.composer/composer.json  
RUN composer global install  
ENV PATH "$HOME/.composer/vendor/bin:$PATH"  
# Install DCR.  
RUN dcr install  
  
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
  
# Install DCIR from local repository.  
COPY . /root/.composer/vendor/decipher/dcir  
RUN cd /root/.composer/vendor/bin && ln -s ../decipher/dcir/dcir dcir  
  
# Setup volume for project.  
VOLUME ["/dcir"]  
  
ENTRYPOINT ["dcir"]

