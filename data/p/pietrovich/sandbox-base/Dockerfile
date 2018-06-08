FROM jsmigel/centos-epel:latest  
MAINTAINER pietrovich@users.noreply.github.com  
  
ADD https://getcomposer.org/composer.phar /usr/bin/composer  
RUN chmod 775 /usr/bin/composer  
  
RUN yum -y install https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
  
ADD https://rpm.nodesource.com/setup_9.x /root/setup-nodejs_9.x.sh  
RUN chmod 770 /root/setup-nodejs_9.x.sh  
RUN [ "/bin/bash", "-c", "/root/setup-nodejs_9.x.sh" ]  
  
ADD https://dl.yarnpkg.com/rpm/yarn.repo /etc/yum.repos.d/yarn.repo  
  
RUN yum -y update  
  
RUN yum -y install \  
yarn \  
redis \  
telnet \  
git \  
bash \  
openssl \  
gcc-c++ \  
make \  
nodejs \  
php71w-cli \  
php71w-fpm \  
php71w-opcache \  
php71w-common \  
php71w-mbstring \  
php71w-mcrypt \  
php71w-mysqlnd \  
php71w-pecl-apcu \  
php71w-pecl-redis \  
php71w-pecl-mongodb \  
php71w-xml \  
php71w-gd \  
php71w-pecl-imagick \  
php71w-phpdbg \  
php71w-pecl-xdebug \  
php71w-devel \  
which \  
psmisc \  
net-tools \  
bind-utils \  
sudo \  
mc  
  
ADD templates/xdebug.ini /etc/php.d/xdebug.ini  
RUN chown root:root /etc/php.d/xdebug.ini  
RUN chmod 0644 /etc/php.d/xdebug.ini  
  
ADD templates/php.ini /etc/php.ini  
RUN chown root:root /etc/php.ini  
RUN chmod 0666 /etc/php.ini  
  
RUN npm install -g npm@^6.0  
RUN npm --version  
RUN yarn --version  
  
RUN npm install -g \  
typescript@^2.8 \  
less \  
webpack@^4.0 \  
node-gyp  
  
RUN npm install node-sass -g --unsafe-perm  
  
RUN yum -y clean all  
RUN rm -rf /var/cache/yum  

