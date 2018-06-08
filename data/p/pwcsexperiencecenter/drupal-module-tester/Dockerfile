FROM openshift/base-centos7  
  
# This image provides an Nginx+PHP environment for testing Drupal 8 modules  
# in a Docker CI environment such as codeship.com  
MAINTAINER Tom Whiston <tom.whiston@pwc-digital.ch>  
  
EXPOSE 8000  
  
ENV PHP_VERSION=7.0 \  
PATH=$PATH:/opt/rh/rh-php70/root/usr/bin  
  
  
ARG BUILD_ENV=test  
ENV DRUPAL_LANGCODE=en \  
DRUPAL_DB_HOST="dmtdb" \  
DRUPAL_DB_TYPE="mysql" \  
DRUPAL_DB_NAME="site" \  
DRUPAL_DB_USER="dbuser" \  
DRUPAL_DB_PASS="dbpass" \  
DRUPAL_DB_PORT=3306 \  
DRUPAL_DB_PREFIX="test" \  
DRUPAL_SITE_NAME="Drupal_Module_Tester" \  
DRUPAL_SITE_MAIL="null@void.com" \  
DRUPAL_ACCOUNT_NAME="admin" \  
DRUPAL_ACCOUNT_MAIL="null@void.com" \  
DRUPAL_ACCOUNT_PASS="t0t4lly1n53cur3"  
LABEL io.k8s.description="PwC's Experience Center - Nginx and PHP 7 (FPM)
Drupal 8 Module Tester" \  
io.k8s.display-name="PwC's Experience Center - Nginx and PHP 7 (FPM) Drupal 8
Module Tester" \  
io.openshift.expose-services="8000:http" \  
io.openshift.tags="builder,nginx,php,php7,php70,php-
fpm,xdebug,pwc,drupal,dev,developer,${BUILD_ENV}"  
  
############################  
# ENVIRONMENTAL CONFIG  
############################  
  
# Each image variant can have an 'env' directory with extra files needed to  
# run and build the applications.  
COPY ./env/${BUILD_ENV} /opt/app-root  
  
# Install Nginx and PHP  
RUN curl 'https://setup.ius.io/' -o setup-ius.sh && \  
bash setup-ius.sh && \  
rm setup-ius.sh && \  
yum install -y --setopt=tsflags=nodocs --enablerepo=centosplus \  
php70u-fpm-nginx \  
php70u-cli \  
php70u-gd \  
php70u-imap \  
php70u-json \  
php70u-mbstring \  
php70u-mcrypt \  
php70u-opcache \  
php70u-pdo \  
php70u-pdo_mysql \  
php70u-xml \  
php70u-curl \  
php70u-xdebug \  
php70u-intl && \  
yum clean all -y && \  
  
cp /opt/app-root/etc/conf.d/php-fpm/pool.conf /etc/php-fpm.d/www.conf && \  
cp /opt/app-root/etc/conf.d/php-fpm/fpm.conf /etc/php-fpm.conf && \  
  
# Xdebug Config  
# We also include a special php.ini which turns on assertions, for ci etc.....  
# by default this is off in the centOS base install  
cp /opt/app-root/etc/conf.d/php-fpm/15-xdebug.ini /etc/php.d/15-xdebug.ini &&
\  
cp /opt/app-root/etc/conf.d/php-fpm/15-xdebug.ini /etc/php-fpm.d/15-xdebug.ini
&& \  
cp /opt/app-root/etc/conf.d/php-fpm/php-asserts.ini /etc/php.ini && \  
  
  
# In order to drop the root user, we have to make some directories world  
# writeable as OpenShift default security model is to run the container under  
# random UID.  
mkdir /tmp/sessions && \  
mkdir -p /opt/app-root/testlog && \  
mkdir -p /opt/app-root/src/app/docroot/sites/simpletest && \  
ln -s /opt/app-root/testlog /opt/app-root/src/app/docroot/sites/simpletest &&
\  
ln -s /opt/app-root/runtime/phpunit.xml /opt/app-
root/src/app/docroot/phpunit.xml && \  
mkdir -p /var/lib/nginx && \  
mkdir -p /var/log/nginx && \  
mkdir -p /opt/app-root/src/app && \  
touch /var/log/nginx/error.log && \  
touch /var/log/nginx/access.log && \  
chown -R 1001:0 /var/log/nginx && \  
chown -R 1001:0 /var/lib/nginx && \  
chown -R 1001:0 /opt/app-root /tmp/sessions && \  
chmod -R a+rwx /tmp/sessions && \  
chmod -R a+rwx /var/log/nginx && \  
chmod -R a+rwx /var/lib/nginx && \  
chmod -R ug+rwx /var/log/nginx && \  
chmod -R ug+rwx /var/lib/nginx && \  
chmod -R ug+rwx /opt/app-root && \  
chmod -R ug+rwx /opt/app-root/testlog && \  
chmod +x /opt/app-root/services.sh && \  
# Create the folders for the module to be tested and symlink it to a more
pleasant location for use in end users files  
mkdir -p /opt/app-root/src/app/docroot/modules/under_test && \  
ln -s /opt/app-root/src/app/docroot/modules/under_test /opt/app-root/test && \  
php -r "readfile('https://getcomposer.org/installer');" | php  
  
# Copy the base app  
COPY ./app /opt/app-root/src/app  
  
#fix permissions to keep the ci happy  
RUN fix-permissions ./  
  
# Switch back to our non root user  
USER 1001  
  
###############  
# DRUPAL SETUP  
###############  
WORKDIR /opt/app-root/src/app  
# Install vendors and generate autoloader  
RUN /opt/app-root/src/composer.phar install  
# Do all our runtime work in our drupal docroot  
WORKDIR /opt/app-root/src/app/docroot  
# Start php-fpm and nginx  
CMD /opt/app-root/services.sh  

