FROM nickbreen/wp-cli:v1.3.1  
MAINTAINER Nick Breen <nick@foobar.net.nz>  
  
ENV WP_DB_ROOT_USER="root" \  
WP_DB_ROOT_PASSWORD="" \  
WP_LOCALE="" \  
WP_DB_HOST="" \  
WP_DB_PORT="" \  
WP_DB_NAME="" \  
WP_DB_USER="" \  
WP_DB_PASSWORD="" \  
WP_DB_PREFIX="" \  
WP_SUBDOMAINS="" \  
WP_URL="" \  
WP_TITLE="" \  
WP_ADMIN_USER="" \  
WP_ADMIN_PASSWORD="" \  
WP_ADMIN_EMAIL="" \  
WP_EXTRA_PHP=""  
RUN mkdir -p /usr/local/share/php/  
COPY php/* /usr/local/share/php/  
  
COPY setup.sh /usr/local/bin/wp-setup  
  
RUN set \- wp-download wp-configure wp-install wp-db-setup wp-commands wp-
sites wp-site-create wp-site-domain wp-safecss; for L; do ln -s
/usr/local/bin/wp-setup /usr/local/bin/$L; done  
  
RUN for f in /usr/local/share/php/*.php; do php -l $f; done && bash -n
/usr/local/bin/wp-setup  
  
WORKDIR /var/www  
  
COPY wp-cli.yml /  

