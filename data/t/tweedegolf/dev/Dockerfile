FROM tweedegolf/php-fpm:7.1.1  
# Install dependencies  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
ruby \  
ruby-dev \  
git \  
htop \  
dnsutils \  
tmux \  
curl \  
wget \  
apt-transport-https \  
python-pip \  
nano \  
vim \  
postgresql-client-$POSTGRESQL_VERSION  
  
# Install nodejs, update npm and install gulp-cli  
ENV NODE_VERSION node_6.x  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
- \  
&& echo "deb https://deb.nodesource.com/$NODE_VERSION jessie main" >
/etc/apt/sources.list.d/nodesource.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
nodejs  
  
ENV NPM_VERSION 4.2.*  
# Fix bug https://github.com/npm/npm/issues/9863  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs.move/
./lib/utils/rename.js  
RUN npm install -g "npm@$NPM_VERSION"  
  
ENV GULP_CLI_VERSION 1.2.*  
RUN npm install -g "gulp-cli@$GULP_CLI_VERSION"  
  
# Install composer  
ENV COMPOSER_VERSION 1.3.1  
RUN curl -o /usr/local/bin/composer
https://getcomposer.org/download/$COMPOSER_VERSION/composer.phar \  
&& chmod a+x /usr/local/bin/composer  
  
# Install sphinx-doc  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
python \  
python-dev \  
python-pip \  
libyaml-dev \  
&& pip install \  
sphinx \  
sphinx-autobuild \  
sphinx-rtd-theme \  
recommonmark  

