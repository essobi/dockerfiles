FROM ubuntu:14.04  
# Replace shell with bash so we can source files  
RUN rm /bin/sh \  
&& ln -s /bin/bash /bin/sh  
  
# Set debconf to run non-interactively  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# Install base dependencies  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
curl \  
zip \  
unzip \  
libssl-dev \  
libfontconfig \  
build-essential \  
wget \  
git-core \  
python-pip \  
jq \  
software-properties-common \  
python-software-properties  
  
# Install aws cli  
RUN pip install awscli  
  
# Add repositories  
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php \  
&& apt-get update  
  
# Install PHP  
ARG PHPVERSION=7.0  
RUN apt-get install -y \  
php$PHPVERSION \  
php$PHPVERSION-curl \  
php$PHPVERSION-common \  
php$PHPVERSION-json \  
php$PHPVERSION-mbstring \  
php$PHPVERSION-xml  
  
# Install Composer  
ENV COMPOSER_HOME /usr/local/bin/.composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer global require hirak/prestissimo:@stable \  
&& composer clear-cache  
  
# Add composer bin to path  
ENV PATH="${COMPOSER_HOME}/vendor/bin:${PATH}"  
# Install Node and NPM  
ARG NVM_DIR=/usr/local/nvm  
ARG NVM_VERSION=0.33.2  
ARG NODE_VERSION=8.1.3  
RUN wget -qO-
https://raw.githubusercontent.com/creationix/nvm/v$NVM_VERSION/install.sh |
bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm use $NODE_VERSION \  
&& n=$(which node) \  
&& n=${n%/bin/node} \  
&& chmod -R 755 $n/bin/* \  
&& cp -r $n/{bin,lib,share} /usr/local \  
&& nvm unload \  
&& rm -rf $NVM_DIR  
  
# Cleanup  
RUN apt-get clean \  
&& rm -rf ~/* /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& history -c  

