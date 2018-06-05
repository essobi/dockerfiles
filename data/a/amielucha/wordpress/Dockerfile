FROM wordpress  
  
# At this stage the code has not been copied to /var/www/html/ yet.  
# Remove default WordPress themes and folders.  
# Install Git.  
# Install WP-CLI.  
# Clone Lightseek theme.  
RUN set -ex; \  
rm -rf /usr/src/wordpress/wp-content/plugins/akismet; \  
rm -rf /usr/src/wordpress/wp-content/plugins/hello.php; \  
rm -rf /usr/src/wordpress/wp-content/themes/twentyfifteen; \  
rm -rf /usr/src/wordpress/wp-content/themes/twentysixteen; \  
rm -rf /usr/src/wordpress/wp-content/themes/twentyseventeen; \  
rm -rf /usr/src/wordpress/readme.html; \  
apt-get update; \  
apt-get install -y --no-install-recommends git sudo; \  
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar; \  
php wp-cli.phar --info; \  
chmod +x wp-cli.phar; \  
sudo mv wp-cli.phar /usr/local/bin/wp; \  
git clone \  
https://github.com/amielucha/lightseek.git \  
/usr/src/wordpress/wp-content/themes/lightseek \  
;  
  
# Add the custom installation script.  
COPY wordpress-install.php /usr/src/wordpress/wp-content/install.php  

