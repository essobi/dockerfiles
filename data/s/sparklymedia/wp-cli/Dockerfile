# WP+WP-CLI based of conetix/docker-wordpress-wp-cli  
FROM wordpress:php5.6-apache  
  
# Add sudo in order to run wp-cli as the www-data user, also install missing
zipArchive support.  
RUN apt-get update && apt-get install -y sudo less mysql-client zlib1g-dev &&
rm -rf /var/lib/apt/lists/* && docker-php-ext-install zip  
# Add WP-CLI  
RUN curl -o /bin/wp-cli.phar https://raw.githubusercontent.com/wp-
cli/builds/gh-pages/phar/wp-cli.phar  
COPY wp-su.sh /bin/wp  
RUN chmod +x /bin/wp-cli.phar /bin/wp  
  
# Cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

