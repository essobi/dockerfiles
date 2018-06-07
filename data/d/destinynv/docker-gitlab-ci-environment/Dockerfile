FROM ubuntu:16.04  
MAINTAINER Michaël Arnauts <michael.arnauts@destiny.be>  
  
ENV DOCKER_VERSION=18.02.0-ce \  
DOCKER_COMPOSE_VERSION=1.19.0 \  
COMPOSER_VERSION=1.6.3 \  
YARN_VERSION=1.5.1 \  
NODEJS_VERSION=8.0  
# Install packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
curl \  
git \  
make \  
php-cli \  
php-curl \  
php-xml \  
php-zip \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
# Install docker  
RUN curl -fsSL https://get.docker.com/ | sh  
  
# Install docker-compose  
RUN curl -L
"https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-
compose-$(uname -s)-$(uname -m)" > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& /usr/local/bin/docker-compose --version  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer --version=$COMPOSER_VERSION \  
&& /usr/local/bin/composer --version  
  
# Add nodejs repository  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
# Add yarn repository  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list  
  
# Install additional packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
nodejs \  
yarn \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  

