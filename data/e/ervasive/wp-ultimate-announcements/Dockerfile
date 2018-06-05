FROM webdevops/php-nginx-dev  
  
# Install required tools  
RUN apt-get update && apt-get install -y mysql-client less \  
&& curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp  
  
# Set working directory & unpriviledged user to install WP  
WORKDIR /app  
USER application  
  
# Setup WordPress installation + plugins  
ARG wp_version="4.7.5"  
ARG wp_plugins_list=" \  
debug-bar \  
debug-bar-cron \  
debug-bar-actions-and-filters-addon \  
user-switching \  
"  
RUN wp core download --version=$wp_version \  
&& wp config create \  
\--dbname=wordpress \  
\--dbuser=wordpress \  
\--dbpass=wordpress \  
\--dbhost=database \  
\--skip-check \  
\--extra-php="define( 'WP_DEBUG', true ); define( 'SAVEQUERIES', true );"  
  
RUN for plugin in $wp_plugins_list; do \  
curl -LOk http://wordpress.org/extend/plugins/download/${plugin}.zip \  
&& unzip -q ${plugin}.zip -d wp-content/plugins \  
&& rm ${plugin}.zip; done  
  
# Reset user  
USER root  
  
  

