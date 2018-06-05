FROM php:7.0.19  
  
ENV NODE_VERSION 6.10.3  
ENV YARN_VERSION 0.24.5  
  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
RUN set -x && \  
apt-get update -yqq && \  
# Common  
mkdir -p ~/.ssh && \  
apt-get install -yqq \  
curl \  
git \  
unzip \  
mariadb-client && \  
# PHP  
apt-get install -yqq \  
libicu-dev \  
libmcrypt-dev \  
libssl-dev \  
zlib1g-dev && \  
pecl install redis mongodb && \  
docker-php-ext-enable redis mongodb && \  
docker-php-ext-install -j$(nproc) \  
bcmath \  
intl \  
mcrypt \  
opcache \  
pcntl \  
pdo_mysql \  
sockets \  
zip && \  
curl -sSL https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
  
# Node / NPM / Yarn  
curl -sSL https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh
| bash && \  
. $NVM_DIR/nvm.sh && \  
nvm install $NODE_VERSION && \  
nvm alias default $NODE_VERSION && \  
nvm use default && \  
npm -g install yarn@${YARN_VERSION} && \  
# Clean  
apt-get purge -y  
  
ADD rootfs /  
  
RUN set -x && \  
php -v && \  
composer --version && \  
node -v && \  
yarn --version  

