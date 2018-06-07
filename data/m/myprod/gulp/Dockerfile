#  
# Gulp image  
#  
FROM node:6  
MAINTAINER Fabien D. <fabien@myprod.net>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
rubygems build-essential ruby-dev ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Gulp & Bower  
RUN npm install -gq gulp bower  
  
# Install Gem Sass  
RUN gem install sass  
  
RUN mkdir -p ${APP_BASE_DIR:-/var/www/}  
  
WORKDIR ${APP_BASE_DIR:-/var/www/}  

