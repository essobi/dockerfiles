FROM ubuntu:16.04  
MAINTAINER Chris Runo <chris.runo@mediacurrent.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL=C.UTF-8  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install;  
  
# Replace shell with bash so we can source files and install packages.  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \  
apt-get update && \  
apt-get -y upgrade; \  
apt-get -y dist-upgrade && \  
apt-get install -y python-software-properties && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:ondrej/php && \  
apt-get update --fix-missing;  
  
# Install basic packages  
RUN apt-get -y install \  
apache2 \  
autoconf \  
automake \  
build-essential \  
bzip2 \  
ca-certificates \  
curl \  
file \  
git \  
imagemagick \  
libfontconfig \  
libfreetype6 \  
libssl-dev \  
make \  
patch \  
vim \  
unzip;  
  
# Install PHP7  
RUN apt-get -y install \  
libapache2-mod-php7.1 \  
php7.1 \  
php7.1-bcmath \  
php7.1-cli \  
php7.1-curl \  
php7.1-dev \  
php7.1-gd \  
php7.1-intl \  
php7.1-json \  
php7.1-mbstring \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-soap \  
php7.1-xml \  
php-imagick \  
php-memcache \  
php-pear;  
  
# Setup and Install MySQL server  
RUN echo "mysql-server mysql-server/root_password password password" |
debconf-set-selections && \  
echo "mysql-server mysql-server/root_password_again password password" |
debconf-set-selections && \  
apt-get -y install mysql-server mysql-client && \  
service mysql start;  
EXPOSE 3306  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/bin;  
RUN composer --verbose self-update --stable;  
  
# Install node and npm  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 6.9.5  
RUN curl --silent -o-
https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash &&
\  
source $NVM_DIR/nvm.sh && \  
nvm install $NODE_VERSION && \  
nvm alias default $NODE_VERSION && \  
nvm use default;  
  
# Add node and npm to path so the commands are available  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
# Install PhantomJS (wernight/phantomjs)  
RUN mkdir /tmp/phantomjs && \  
curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
| tar -xj --strip-components=1 -C /tmp/phantomjs && \  
mv /tmp/phantomjs/bin/phantomjs /usr/local/bin;  
  
# Install NPM modules  
RUN npm install -g pa11y@4.13.2 && \  
npm install -g slack-cli && \  
npm install -g forever;  
  
# Clean up installs  
RUN apt-get autoclean && apt-get clean && apt-get autoremove;  
RUN rm -rf /root/.composer /tmp/*  
  
CMD bash  

