FROM php:5.6-apache  
MAINTAINER Dan Lobelle <daniel.lobelle@wmich.edu>  
  
RUN a2enmod rewrite  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql zip  
  
# Install MySQL.  
RUN echo mysql-server mysql-server/root_password select root | debconf-set-
selections  
RUN echo mysql-server mysql-server/root_password_again select root | debconf-
set-selections  
RUN apt-get update && apt-get install -y mysql-server  
  
# Install Composer.  
RUN apt-get update && apt-get install -y wget && \  
EXPECTED_SIGNATURE=$(wget https://composer.github.io/installer.sig -O - -q);
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');";
ACTUAL_SIGNATURE=$(php -r "echo hash_file('SHA384', 'composer-setup.php');");
if [ "$EXPECTED_SIGNATURE" = "$ACTUAL_SIGNATURE" ]; then php composer-
setup.php --quiet; RESULT=$?; rm composer-setup.php; mv composer.phar
/usr/local/bin/composer; exit $RESULT; else >&2 echo 'ERROR: Invalid installer
signature'; rm composer-setup.php; exit 1; fi  
  
# Install Drush with Composer (because PHP_OPTIONS, below, doesn't seem to
work with drush.phar).  
RUN mkdir --parents /opt/drush && \  
cd /opt/drush && \  
composer init --require=drush/drush:8.* -n && \  
composer config bin-dir /usr/local/bin && \  
composer install  
  
# Install Drupal.  
WORKDIR /var/www/html  
# https://www.drupal.org/node/3060/release  
ENV DRUPAL_VERSION 7.53  
ENV DRUPAL_MD5 4230279ecca4f0cde652a219e10327e7  
RUN curl -fSL
"http://ftp.drupal.org/files/projects/drupal-${DRUPAL_VERSION}.tar.gz" -o
drupal.tar.gz \  
&& echo "${DRUPAL_MD5} *drupal.tar.gz" | md5sum -c - \  
&& tar -xz --strip-components=1 -f drupal.tar.gz \  
&& rm drupal.tar.gz \  
&& chown -R www-data:www-data sites  
RUN service mysql start && \  
/usr/bin/env PHP_OPTIONS="-d sendmail_path=`which true`" drush site-install
--yes --db-su=root --db-su-pw=root --db-
url=mysql://drupal:drupal@127.0.0.1/drupal --account-name=testbot --account-
pass=testbot minimal && \  
chown www-data.www-data /var/www/html/sites/default/files && \  
chmod 2775 /var/www/html/sites/default/files && \  
mkdir -p /var/www/private-files && \  
chown www-data.www-data /var/www/private-files && \  
chmod 2775 /var/www/private-files && \  
drush variable-set --yes file_private_path /var/www/private-files  
  
# Install rsync.  
RUN apt-get update && apt-get install -y rsync  
  
# Install Selenium for JavaScript-enabled Behat tests.  
RUN apt-get update && apt-get install -y openjdk-7-jre-headless iceweasel xvfb
&& \  
wget "http://selenium-release.storage.googleapis.com/2.53/selenium-server-
standalone-2.53.0.jar" && \  
mv selenium-server-standalone-2.53.0.jar /usr/local/bin/selenium-server-
standalone.jar  
  
# Create a mount point for the project directory.  
RUN mkdir -p /project/test-reports  
VOLUME /project  
  
# Create a directory for mounting libraries.  
RUN mkdir -p /var/www/html/sites/all/libraries  
  
# Add the start script.  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
# Add the alternative start script for site testing.  
ADD ./start-site.sh /start-site.sh  
RUN chmod 755 /start-site.sh  
  
# Set environment defaults.  
ENV TEST_MODE behat  
ENV BEHAT_PARAMETERS --no-interaction --format=junit --format=pretty  
ENV MODULES_DIR /var/www/html/sites/all/modules  
ENV PROFILE minimal  
  
# Run the start script.  
CMD ["/bin/bash", "/start.sh"]  

