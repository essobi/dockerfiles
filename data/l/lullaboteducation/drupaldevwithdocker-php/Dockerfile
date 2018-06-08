FROM ubuntu:xenial  
  
################################################################################  
# #  
# THIS CONTAINER IS FOR EDUCATIONAL USE ONLY! #  
# #  
# Never use this container for running production workloads! #  
# #  
################################################################################  
# Update the package manager, then install packages.  
RUN apt-get update && \  
apt-get install -y \  
apache2 \  
php7.0 \  
libapache2-mod-php7.0 \  
php7.0-mysql \  
php7.0-cli \  
php7.0-common \  
php7.0-gd \  
php7.0-mbstring \  
php7.0-xml \  
php7.0-opcache \  
php7.0-sqlite3 \  
php7.0-mysql \  
php7.0-curl \  
php7.0-soap \  
mariadb-client  
  
# Replace the default site configuration with our own.  
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf  
  
# Enable mod_rewrite 'cause we needs it.  
RUN a2enmod rewrite  
  
# Forward logs to docker log collector.  
RUN ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log && \  
ln -sf /dev/stdout /var/log/apache2/000_default-access_log && \  
ln -sf /dev/stderr /var/log/apache2/000_default-error_log  
  
# Copy our custom entrypoint and make it executable.  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
# Expose the default Apache port.  
EXPOSE 80  
# Replace the standard entrypoint /bin/sh with our script.  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
# If no command is passed to the container, start Apache by default.  
CMD ["apachectl", "-D", "FOREGROUND"]  

