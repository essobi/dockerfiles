# Selesti modern stack  
FROM 1and1internet/ubuntu-16-apache-php-7.2  
MAINTAINER Owen Melbourne <owen@selesti.com>  
RUN apt update  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository ppa:git-core/ppa  
RUN apt-get install -y git  
  
# PHP Tools  
RUN composer global require "squizlabs/php_codesniffer=*"  
RUN composer global require "phpunit/phpunit=7.1.*"  
  
# Configure Node  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g eslint sass-lint node-sass gulp-cli grunt-cli yarn bower  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
RUN npm rebuild node-sass  

