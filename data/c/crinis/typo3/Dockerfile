FROM crinis/php-for-typo3:7.1-fpm-alpine-8.7  
ENV COMPOSER_CONFIG_DIR="/code" \  
COMPOSER_UPDATE="true" \  
DEFAULT_HTACCESS="true" \  
TYPO3_DB_HOST="db" \  
TYPO3_DB_PORT="3306" \  
TYPO3_DB_NAME="typo3" \  
TYPO3_DB_USER="typo3" \  
TYPO3_DB_PASSWORD="password" \  
TYPO3_FIRST_INSTALL="true" \  
TYPO3_SITE_NAME="TYPO3 CMS" \  
TYPO3_INTRODUCTION_PACKAGE="true" \  
TYPO3_EXTENSION_ACTIVATION_LIST="about,belog,beuser,context_help,documentation,filemetadata,func,info,info_pagetsconfig,lowlevel,opendocs,reports,rsaauth,setup,sys_action,sys_note,t3editor,taskcenter,tstemplate,version,viewpage,wizard_crpages,wizard_sortpages"
\  
TYPO3_INSTALL_TOOL_PASSWORD="" \  
TYPO3_ADMIN_USER="admin" \  
TYPO3_ADMIN_PASSWORD="password" \  
TYPO3_DB_HOST_FILE="" \  
TYPO3_DB_PORT_FILE="" \  
TYPO3_DB_NAME_FILE="" \  
TYPO3_DB_USER_FILE="" \  
TYPO3_DB_PASSWORD_FILE="" \  
TYPO3_INSTALL_TOOL_PASSWORD_FILE="" \  
TYPO3_ADMIN_USER_FILE="" \  
TYPO3_ADMIN_PASSWORD_FILE=""  
COPY composer-default.json /composer-default.json  
COPY composer-introduction-package.json /composer-introduction-package.json  
COPY typo3-scheduler-crontab /typo3-scheduler-crontab  
COPY typo3-htaccess /typo3-htaccess  
COPY AdditionalConfiguration.php /AdditionalConfiguration.php  
COPY typo3-docker-entrypoint.sh /usr/local/bin/typo3-docker-entrypoint.sh  
COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh  
  
RUN set -xe \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& chmod +x /usr/local/bin/typo3-docker-entrypoint.sh /usr/local/bin/wait-for-
it.sh \  
&& /usr/bin/crontab -u www-data /typo3-scheduler-crontab  
  
WORKDIR $COMPOSER_CONFIG_DIR  
  
ENTRYPOINT ["typo3-docker-entrypoint.sh"]  
  
CMD ["php-fpm"]  

