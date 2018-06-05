FROM ubuntu:16.04  
MAINTAINER Artful Solutions <docker@artfulsolutions.de>  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Install PHP + PHP Extensions  
RUN apt-get update && apt-get -y install locales wget git zip curl build-
essential php7.0 php7.0-mysql php7.0-curl php7.0-sqlite php7.0-mcrypt
php7.0-xml php7.0-gd php7.0-mbstring php7.0-json php7.0-zip php-xdebug  
RUN locale-gen en_US.UTF-8  
  
# Install Composer  
RUN [ ! -f "composer.phar" ] && wget https://getcomposer.org/composer.phar  
RUN mv composer.phar /usr/local/bin/composer  
RUN /bin/chmod +x /usr/local/bin/composer  
  
# Install NPM  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash  
RUN apt-get -y install nodejs  
  
# Debian installs `node` as `nodejs`  
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10  
  
# Install Ruby for Sass  
RUN apt-get -y install ruby-dev  
  
RUN apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Install Sass  
RUN gem install sass  
  
EXPOSE 8008  
WORKDIR /tmp/code

