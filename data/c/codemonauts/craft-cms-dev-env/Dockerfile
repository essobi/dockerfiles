FROM ubuntu:xenial  
ENV DEBIAN_FRONTEND noninteractive  
ENV NODE_VERSION 9.11.1  
ENV NVM_DIR /root/.nvm  
RUN apt-get update && apt-get -uy upgrade  
RUN apt-get -y install locales ruby-dev git zip vim rsync ruby iwatch nginx
php7.0-fpm php7.0-zip php7.0-intl php7.0-cli php7.0-mysql php7.0-curl
php7.0-gd php-imagick php7.0-mcrypt php7.0-mbstring mysql-client php-soap php-
xml curl build-essential autoconf autogen libtool  
RUN phpenmod mcrypt  
RUN locale-gen en_US.UTF-8  
RUN mkdir /local  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash  
RUN . ~/.nvm/nvm.sh && nvm install $NODE_VERSION && nvm alias default
$NODE_VERSION && npm install --global gulp-cli pug-cli bower postcss-cli
autoprefixer uglify-js  
RUN ln -sf /local/craft/app/etc/console/yiic /usr/local/bin/yiic  
RUN gem update --system  
RUN gem install sass  
RUN gem install compass  
RUN cd /usr/local/bin; curl --silent --show-error
https://getcomposer.org/installer | php; mv composer.phar composer  
ADD includes /  
CMD . /run.sh  

