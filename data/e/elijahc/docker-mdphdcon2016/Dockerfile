FROM webdevops/php-nginx  
  
MAINTAINER Elijah Christensen <elijah.christensen@ucdenver.edu>  
  
# Install dependencies  
RUN apt-get update && \  
apt-get install wget vim && \  
wget
https://raw.githubusercontent.com/composer/getcomposer.org/e67dc80d23742dd8ad67fa63135d7f8fdf2e2fb6/web/installer
-O - -q | php -- --quiet  

