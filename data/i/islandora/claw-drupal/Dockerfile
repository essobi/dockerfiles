FROM islandora/claw-base  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="MIT" \  
"Version"="0.0.1"  
  
EXPOSE 80  
ARG DRUPAL_VERSION="7.43"  
ARG DRUSH_VERSION="8.0.2"  
ENV DRUPAL_ROOT=/var/www/localhost/htdocs  
  
WORKDIR ${DRUPAL_ROOT}  
  
RUN apk-install git apache2 apache2-utils apache2-proxy mysql-client \  
php-apache2 php-mysql php-gd php-xml php-soap php-posix php-phar \  
php-openssl php-json php-ctype php-pdo php-pdo_mysql php-curl php-pear \  
php-xsl php-xmlreader && \  
mkdir /run/apache2 && \  
chown -R apache:apache /var/www && \  
chmod 2775 /var/www/localhost && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin && \  
mv /usr/local/bin/composer.phar /usr/local/bin/composer && \  
chmod a+x /usr/local/bin/composer && \  
curl -L -o /usr/local/bin/drush https://github.com/drush-
ops/drush/releases/download/${DRUSH_VERSION}/drush.phar && \  
chmod a+x /usr/local/bin/drush && \  
s6-setuidgid apache drush dl -y --destination=/var/www/localhost --drupal-
project-rename=htdocs drupal-${DRUPAL_VERSION} && \  
s6-setuidgid apache mkdir ${DRUPAL_ROOT}/sites/all/modules/contrib \  
${DRUPAL_ROOT}/sites/all/modules/custom \  
${DRUPAL_ROOT}/sites/all/modules/features && \  
cleanup  
  
COPY rootfs /  

