FROM jantoine/drupal:7  
  
# Install Composer.  
RUN set -ex; \  
\  
COMPOSER_SIGNATURE=$(curl https://composer.github.io/installer.sig); \  
curl -fSL "https://getcomposer.org/installer" -o composer-setup.php; \  
echo "${COMPOSER_SIGNATURE} composer-setup.php" | sha384sum -c -; \  
php composer-setup.php; \  
rm composer-setup.php; \  
mv composer.phar /usr/local/bin/composer  
  
# Install GIT.  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y --no-install-recommends \  
git \  
openssh-client \  
; \  
rm -rf /var/lib/apt/lists/*  
  
# Configure PHP for development.  
RUN set -ex; \  
\  
# Disable PHP's opcache extension so code changes take effect immediately.  
rm /usr/local/etc/php/conf.d/opcache-recommended.ini; \  
rm /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini; \  
\  
{ \  
echo 'max_execution_time=0'; \  
echo 'max_input_vars = 2000'; \  
echo 'memory_limit=-1'; \  
echo 'post_max_size=0'; \  
echo 'upload_max_filesize=0'; \  
} >> /usr/local/etc/php/php.ini;  
  
# Install Xdebug.  
RUN set -ex; \  
\  
pecl install xdebug; \  
{ \  
echo 'zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20151012/xdebug.so'; \  
echo 'xdebug.remote_enable=1'; \  
echo 'xdebug.remote_autostart=0'; \  
echo 'xdebug.remote_connect_back=1'; \  
echo 'xdebug.remote_port=9000'; \  
} > /usr/local/etc/php/conf.d/ext-xdebug.ini  
  
# Install Coder.  
RUN set -ex; \  
\  
export COMPOSER_HOME="/usr/local/composer"; \  
composer global require drupal/coder; \  
echo '' | tee -a ~/.bashrc /etc/skel/.bashrc; \  
echo '# Include global composer binaries in PATH.' | tee -a ~/.bashrc
/etc/skel/.bashrc; \  
echo 'export PATH="$PATH:/usr/local/composer/vendor/bin"' | tee -a ~/.bashrc
/etc/skel/.bashrc; \  
export PATH="$PATH:/usr/local/composer/vendor/bin"; \  
phpcs --config-set installed_paths
/usr/local/composer/vendor/drupal/coder/coder_sniffer; \  
{ \  
echo ''; \  
echo '# Custom phpcs aliases.'; \  
echo "alias drupalcs=\"phpcs --standard=Drupal
--extensions='php,module,inc,install,test,profile,theme,css,info,txt,md'
--ignore=*\.bean.inc,*\.context.inc,*\.current_search.inc,*\.default_breakpoint_group.inc,*\.default_breakpoints.inc,*\.default_picture_mapping.inc,*\.entityqueue_default.inc,*\.facetapi_defaults.inc,*\.features.commerce_checkout_panes.inc,*\.features.field_base.inc,*\.features.field_instance.inc,*\.features.filter.inc,*\.features.inc,*\.features.media_wysiwyg.inc,*\.features.taxonomy.inc,*\.features.user_permission.inc,*\.features.user_role.inc,*\.features.wysiwyg.inc,*\.field_group.inc,*\.file_default_displays.inc,*\.file_type.inc,*\.flexslider_default_preset.inc,*\.flexslider_picture_optionset.inc,*\.rules_defaults.inc,*\.strongarm.inc,*\.views_default.inc,*/themes/custom/*\.css\"";
\  
echo "alias drupalcsp=\"phpcs --standard=DrupalPractice
--extensions='php,module,inc,install,test,profile,theme,css,info,txt,md'
--ignore=*\.bean.inc,*\.context.inc,*\.current_search.inc,*\.default_breakpoint_group.inc,*\.default_breakpoints.inc,*\.default_picture_mapping.inc,*\.entityqueue_default.inc,*\.facetapi_defaults.inc,*\.features.commerce_checkout_panes.inc,*\.features.field_base.inc,*\.features.field_instance.inc,*\.features.filter.inc,*\.features.inc,*\.features.media_wysiwyg.inc,*\.features.taxonomy.inc,*\.features.user_permission.inc,*\.features.user_role.inc,*\.features.wysiwyg.inc,*\.field_group.inc,*\.file_default_displays.inc,*\.file_type.inc,*\.flexslider_default_preset.inc,*\.flexslider_picture_optionset.inc,*\.rules_defaults.inc,*\.strongarm.inc,*\.views_default.inc,*/themes/custom/*\.css\"";
\  
echo "alias drupalcbf=\"phpcbf --standard=Drupal
--extensions='php,module,inc,install,test,profile,theme,css,info,txt,md'
--ignore=*\.bean.inc,*\.context.inc,*\.current_search.inc,*\.default_breakpoint_group.inc,*\.default_breakpoints.inc,*\.default_picture_mapping.inc,*\.entityqueue_default.inc,*\.facetapi_defaults.inc,*\.features.commerce_checkout_panes.inc,*\.features.field_base.inc,*\.features.field_instance.inc,*\.features.filter.inc,*\.features.inc,*\.features.media_wysiwyg.inc,*\.features.taxonomy.inc,*\.features.user_permission.inc,*\.features.user_role.inc,*\.features.wysiwyg.inc,*\.field_group.inc,*\.file_default_displays.inc,*\.file_type.inc,*\.flexslider_default_preset.inc,*\.flexslider_picture_optionset.inc,*\.rules_defaults.inc,*\.strongarm.inc,*\.views_default.inc,*/themes/custom/*\.css\"";
\  
echo "alias gitcs=\"drupalcs $(git diff --name-only | tr '\n' ' ')\""; \  
} | tee -a ~/.bashrc /etc/skel/.bashrc  
  
# Install Node.js 8.x.  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y --no-install-recommends \  
gnupg \  
;\  
curl -sL https://deb.nodesource.com/setup_8.x | bash -; \  
apt-get install -y --no-install-recommends \  
nodejs \  
; \  
rm -rf /var/lib/apt/lists/*  
  
# Install RVM, ruby and bundler.  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y --no-install-recommends \  
dirmngr \  
sudo \  
; \  
rm -rf /var/lib/apt/lists; \  
export LANG="en_US.UTF-8"; \  
gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3
7D2BAF1CF37B13E2069D6956105BD0E739499BDB; \  
addgroup --system rvm; \  
\curl -sSL https://get.rvm.io | sudo bash -s stable; \  
/bin/bash -l -c ". /etc/profile.d/rvm.sh && rvm install ruby --latest && gem
install bundler && rvm fix-permissions"  
  
# Copy scripts.  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["apache2-foreground"]  

