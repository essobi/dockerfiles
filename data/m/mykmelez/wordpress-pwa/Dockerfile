# https://github.com/docker-library/wordpress/blob/master/apache/Dockerfile  
FROM wordpress:latest  
  
# Install the software packages we need to build/install the Wordpress
plugins.  
#  
# We link /usr/local/bin/node to /usr/bin/nodejs to ensure it's available  
# at that name for Node scripts with `#!/usr/bin/env node` shebangs.  
#  
# We install the PHP "composer" utility only for wp-add-to-homescreen, as both  
# wp-web-push and wp-offline-shell install their own copy of that utility.  
#  
RUN apt-get update && apt-get install -y \  
git \  
node \  
npm \  
unzip \  
wget \  
zip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& ln -s /usr/bin/nodejs /usr/local/bin/node \  
&& npm install -g bower \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Build and install wp-web-push.  
COPY wp-web-push /var/tmp/wp-web-push  
RUN cd /var/tmp/wp-web-push/ \  
&& make build \  
&& unzip wp-web-push.zip -d /usr/src/wordpress/wp-content/plugins/wp-web-push
\  
&& chown -R www-data:www-data /usr/src/wordpress/wp-content/plugins/wp-web-
push \  
&& rm -rf /var/tmp/wp-web-push  
  
# Build and install wp-offline-shell.  
COPY offline-shell /var/tmp/wp-offline-shell  
RUN cd /var/tmp/wp-offline-shell/ \  
&& make build \  
&& unzip wp-offline-shell.zip -d /usr/src/wordpress/wp-content/plugins/wp-
offline-shell \  
&& chown -R www-data:www-data /usr/src/wordpress/wp-content/plugins/wp-
offline-shell \  
&& rm -rf /var/tmp/wp-offline-shell  
  
# Build and install wp-add-to-homescreen.  
COPY wp-add-to-homescreen/wp-add-to-homescreen /usr/src/wordpress/wp-
content/plugins/wp-add-to-homescreen  
RUN cd /usr/src/wordpress/wp-content/plugins/wp-add-to-homescreen/ \  
&& composer install --optimize-autoloader \  
&& bower --allow-root install \  
&& chown -R www-data:www-data /usr/src/wordpress/wp-content/plugins/wp-add-to-
homescreen  
  
# Install the WP Force SSL plugin so you can force users to the encrypted  
# variant of your WordPress website. This installs the plugin, but it doesn't  
# activate it by default, so you can use this Docker image locally without SSL  
# during development and then activate the plugin in production.  
RUN curl -LO https://downloads.wordpress.org/plugin/wp-force-ssl.zip \  
&& unzip wp-force-ssl.zip \  
&& rm wp-force-ssl.zip \  
&& chown -R www-data:www-data wp-force-ssl \  
&& mv wp-force-ssl /usr/src/wordpress/wp-content/plugins/  

