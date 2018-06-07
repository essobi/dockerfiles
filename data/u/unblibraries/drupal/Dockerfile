FROM unblibraries/nginx-php:alpine-php7  
MAINTAINER Jacob Sanford <libsystems_at_unb.ca>  
  
LABEL ca.unb.lib.generator="drupal8"  
LABEL vcs-ref="alpine-nginx-php7-8.x"  
LABEL vcs-url="https://github.com/unb-libraries/docker-drupal"  
  
ENV DRUPAL_ADMIN_ACCOUNT_NAME admin  
ENV DRUPAL_CONFIGURATION_DIR ${APP_ROOT}/configuration  
ENV DRUPAL_CONFIGURATION_EXPORT_SKIP devel  
ENV DRUPAL_DEPLOY_CONFIGURATION FALSE  
ENV DRUPAL_INSTALL_REMOVE_SHORTCUT TRUE  
ENV DRUPAL_REBUILD_ON_REDEPLOY TRUE  
ENV DRUPAL_REVERT_FEATURES FALSE  
ENV DRUPAL_ROOT $APP_WEBROOT  
ENV DRUPAL_SITE_ID defaultd  
ENV DRUPAL_SITE_UUID FALSE  
ENV DRUPAL_TESTING_TOOLS FALSE  
ENV DRUPAL_TESTING_ROOT ${APP_ROOT}/tests  
ENV DRUPAL_UNIT_TEST_CLASSES "\Drupal\node\Tests\PagePreviewTest
\Drupal\file\Tests\FilePrivateTest"  
ENV RSYNC_FLAGS --stats  
ENV TERM dumb  
ENV TMP_DRUPAL_BUILD_DIR /tmp/drupal_build  
ENV DRUPAL_BUILD_TMPROOT ${TMP_DRUPAL_BUILD_DIR}/webroot  
  
# Install required packages, libraries.  
RUN apk --update add php7-mysqlnd php7-session php7-pdo php7-pdo_mysql \  
php7-pcntl php7-dom php7-posix php7-ctype php7-gd php7-xml php7-opcache \  
php7-mbstring php7-tokenizer php7-simplexml php7-xmlwriter git unzip \  
php7-dom mysql-client rsync && \  
rm -f /var/cache/apk/*  
  
# Add package conf, create build location.  
COPY ./conf /conf  
RUN cp /conf/nginx/app.conf /etc/nginx/conf.d/app.conf && \  
cp /conf/php/app-php.ini /etc/php7/conf.d/zz_app.ini && \  
cp /conf/php/app-php-fpm.conf /etc/php7/php-fpm.d/zz_app.conf && \  
rm -rf /conf && \  
mkdir -p ${TMP_DRUPAL_BUILD_DIR}  
  
# Copy profile, settings to container.  
COPY ./build/ ${TMP_DRUPAL_BUILD_DIR}  
  
# Tests.  
COPY ./tests ${DRUPAL_TESTING_ROOT}  
  
# Copy scripts to container, build tree.  
COPY ./scripts /scripts  
ARG DRUPAL_COMPOSER_DEV=no-dev  
RUN /scripts/buildDrupalTree.sh ${DRUPAL_COMPOSER_DEV} && \  
/scripts/installDevTools.sh ${DRUPAL_COMPOSER_DEV} && \  
cp /scripts/drupalCron.sh /etc/periodic/15min/drupalCron  
  
# Volumes  
VOLUME /app/html/sites/default  

