FROM wordpress  
  
RUN apt-get update -y && apt-get -y install apt-utils php5-ldap libldap2-dev
ldap-utils  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu &&
docker-php-ext-install ldap && a2enmod rewrite  
  
RUN mkdir bbpress  
COPY bbpress/ /usr/src/wordpress/wp-content/plugins/bbpress/  
  
RUN mkdir buddypress  
COPY buddypress/ /usr/src/wordpress/wp-content/plugins/buddypress/  
  
RUN mkdir ldap-login-password-and-role-manager  
COPY ldap-login-password-and-role-manager/ /usr/src/wordpress/wp-
content/plugins/ldap-login-password-and-role-manager/  
  
RUN mkdir wp-useronline  
COPY wp-useronline/ /usr/src/wordpress/wp-content/plugins/wp-useronline/  
  
RUN mkdir buddypress-docs  
COPY buddypress-docs/ /usr/src/wordpress/wp-content/plugins/buddypress-docs/  
  
RUN mkdir easy-wp-smtp/  
COPY easy-wp-smtp/ /usr/src/wordpress/wp-content/plugins/easy-wp-smtp/  
  
RUN mkdir socialize-lite/  
COPY socialize-lite/ /usr/src/wordpress/wp-content/themes/socialize-lite/  
  
RUN mkdir buddydrive/  
COPY buddydrive/ /usr/src/wordpress/wp-content/plugins/buddydrive/  
  
RUN chown -R www-data:www-data /usr/src/wordpress/wp-content/plugins  
RUN chown -R www-data:www-data /usr/src/wordpress/wp-content/themes  

