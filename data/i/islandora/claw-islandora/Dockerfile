FROM islandora/claw-drupal  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="MIT" \  
"Version"="0.0.1"  
  
ENV DRUPAL_SITE_INSTALL_PROFILE="claw_install_profile"  
  
# This is a temporary measure until we create our own APK package for
php5-stomp  
RUN apk-install make autoconf gcc openssl-dev php-dev libc-dev bash && \  
touch /etc/php/conf.d/stomp.ini && \  
pear config-set php_ini /etc/php/conf.d/stomp.ini && \  
pear install pecl/stomp && \  
pear config-set php_ini /etc/php/php.ini && \  
apk-uninstall make autoconf gcc openssl-dev php-dev libc-dev bash && \  
cleanup  
  
# Download Drupal module dependencies.  
RUN curl -L https://github.com/Islandora-
CLAW/claw_install_profile/archive/master.tar.gz | \  
tar -xzf - -C ${DRUPAL_ROOT}/profiles && \  
mv ${DRUPAL_ROOT}/profiles/claw_install_profile-master
${DRUPAL_ROOT}/profiles/claw_install_profile && \  
mkdir ${DRUPAL_ROOT}/sites/all/libraries/ARC2 && \  
cd ${DRUPAL_ROOT} && drush make -y --concurrency=4 \--no-cache \  
${DRUPAL_ROOT}/profiles/claw_install_profile/claw_install_profile.make && \  
mv ${DRUPAL_ROOT}/sites/all/libraries/ARC2/arc2
${DRUPAL_ROOT}/sites/all/libraries/ARC2/arc && \  
cleanup  
  
# This is a temporary measure until we split up the repo into sub-modules.  
# We will eventually make it part of the drush make file like everything else.  
RUN git clone https://github.com/Islandora-CLAW/islandora.git /opt/islandora
&& \  
ln -s /opt/islandora ${DRUPAL_ROOT}/sites/all/modules/islandora && \  
chmod -R a+rx /opt/islandora && \  
chown -R apache:apache /opt/islandora && \  
chmod -R g+rw /opt/islandora  
  
COPY rootfs /  

