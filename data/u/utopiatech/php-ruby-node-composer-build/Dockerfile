FROM ubuntu:16.04  
MAINTAINER Utopia <tech@utopia.de>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
ENV COMPOSER_NO_INTERACTION 1  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
curl \  
apt-transport-https \  
ca-certificates \  
gnupg2 \  
&& curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
- \  
&& echo "deb https://deb.nodesource.com/node_8.x jessie main" >
/etc/apt/sources.list.d/nodesource.list \  
# Install tools  
&& apt-get update \  
&& apt-get install --no-install-recommends -y \  
openssh-client \  
bzip2 \  
unzip \  
git \  
php7.0-cli \  
php7.0-zip \  
nodejs \  
rsync \  
locales \  
ruby \  
ruby-dev \  
bundler \  
libfreetype6 \  
libfontconfig \  
build-essential \  
# Slim down image \  
&& apt-get autoclean && apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/??
/usr/share/man/??_*  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install node tools  
RUN npm install -g grunt-cli bower  
  
# Show versions  
RUN php -v  
RUN node -v  
RUN npm -v  
RUN ruby -v  
RUN bundle -v  
RUN grunt --version  
RUN bower --allow-root --version  

