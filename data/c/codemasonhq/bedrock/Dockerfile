FROM codemasonhq/php:base  
  
# Install WP CLI and DotEnv command  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& chmod +x wp-cli.phar && mv wp-cli.phar /usr/local/bin/wp \  
&& php -d memory_limit=-1 /usr/local/bin/wp --allow-root package install
aaemnnosttv/wp-cli-dotenv-command:^1.0  
  
# Add project files  
ONBUILD COPY . /app  
  
# Install dependencies  
ONBUILD RUN composer install  

