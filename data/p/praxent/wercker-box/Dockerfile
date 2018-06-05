FROM php:5.6.21-fpm  
MAINTAINER John Z Black <john@praxent.com>  
RUN apt-get update && apt-get install -y \  
php5-gd \  
git \  
automake \  
build-essential \  
libssl-dev \  
zip \  
curl \  
nodejs \  
npm \  
ruby \  
ruby-dev  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g bower && \  
npm install -g grunt-cli && \  
npm install -g node-sass  
RUN rm -rf /var/lib/apt/lists/*  
RUN echo date.timezone="America/Chicago" >> /usr/local/etc/php/conf.d/php.ini  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /bin/composer  
RUN gem install bundler rubygems-bundler --no-rdoc --no-ri  
RUN bundle config --global silence_root_warning 1  
RUN gem regenerate_binstubs  

