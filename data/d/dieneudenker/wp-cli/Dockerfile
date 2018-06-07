FROM php:7.1.11-cli-jessie  
  
# Refresh apt repository  
RUN apt-get update  
  
# Install mysqli extension for PHP  
RUN docker-php-ext-install mysqli  
  
# Install WP-CLI and mysql client (needed for WP-CLI database commands)  
RUN mkdir /wp-cli && \  
cd /wp-cli && \  
apt-get -qq install curl && \  
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && \  
chmod +x wp-cli.phar && \  
mv wp-cli.phar /usr/local/bin/wp  
RUN apt-get -qq install mysql-client  
  
# Copy and run startup file  
COPY startup.sh /startup/  
RUN chmod 700 /startup/startup.sh  
CMD /startup/startup.sh  
  
# Set workdir  
WORKDIR /app

