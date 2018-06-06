FROM davidedimauro88/apache_php5  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y openssh-client \  
mysql-client \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
RUN apt-get update && \  
apt-get install -y locales -qq \  
\--no-install-recommends && rm -r /var/lib/apt/lists/* &&\  
locale-gen en_GB.UTF-8 en_gb && \  
dpkg-reconfigure locales &&\  
dpkg-reconfigure locales &&\  
locale-gen C.UTF-8 &&\  
/usr/sbin/update-locale LANG=C.UTF-8  
  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
  
RUN a2enmod rewrite \  
remoteip \  
headers \  
expires \  
deflate \  
proxy \  
proxy_fcgi  
  
RUN apt-get update && \  
apt-get install -y php5-mysql \  
php5-curl \  
php5-cli \  
php5-gd \  
imagemagick \  
php5-memcache \  
php5-dev \  
php5-imagick \  
php-pear \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
#Install nodejs  
RUN wget https://nodejs.org/dist/v4.4.3/node-v4.4.3-linux-x64.tar.xz && \  
tar xf node-v4.4.3-linux-x64.tar.xz && \  
mv node-v4.4.3-linux-x64 /var/lib/nodejs && \  
ln -s /var/lib/nodejs/bin/node /usr/local/bin/node && \  
ln -s /var/lib/nodejs/bin/npm /usr/local/bin/npm && \  
node --version && \  
npm version  
  
#Install phing and drush  
RUN composer require phing/phing:2.* && \  
composer require drush/drush:8.1 && \  
cd vendor/drush/drush && composer install  
RUN mv vendor /var/lib/composer-modules && \  
ln -s /var/lib/composer-modules/bin/drush /usr/local/bin/drush && \  
ln -s /var/lib/composer-modules/bin/phing /usr/local/bin/phing && \  
phing -v && drush --version  
  
#Install grunt cli  
RUN npm install -g grunt-cli && \  
ln -s /var/lib/nodejs/lib/node_modules/grunt-cli/bin/grunt
/usr/local/bin/grunt && \  
grunt --version  
  
#Install RVM  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 &&\  
\curl https://raw.githubusercontent.com/rvm/rvm/master/binscripts/rvm-
installer | bash -s stable &&\  
\curl -sSL https://get.rvm.io | bash -s stable &&\  
\curl -sSL https://get.rvm.io | bash &&\  
\curl -sSL https://get.rvm.io | bash -s -- --ignore-dotfiles &&\  
\curl -sSL https://get.rvm.io | bash -s stable &&\  
echo "source /usr/local/rvm/scripts/rvm" >> /root/.bashrc &&\  
bash -l -c "rvm install 2.1.5" &&\  
bash -l -c "rvm install 2.3.0" &&\  
bash -l -c "rvm use --default 2.1.5"  

