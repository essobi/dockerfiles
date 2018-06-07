FROM library/node:7.8  
MAINTAINER Robin Bonin <robin@bonin.nu>  
  
# Install dumb-init to be able to kill the container  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64  
RUN chmod +x /usr/local/bin/dumb-init  
  
# Install Gulp  
RUN npm install -g gulp-cli node-sass  

