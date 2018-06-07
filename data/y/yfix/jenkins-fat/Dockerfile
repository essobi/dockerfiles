FROM yfix/jenkins  
  
# if we want to install via apt  
USER root  
  
ENV COMPOSER_HOME "/usr/local/share/composer"  
ENV PATH $PATH:$COMPOSER_HOME/vendor/bin/  
ENV DEBIAN_FRONTEND noninteractive  
  
# Bash as default shell  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
COPY ansible /tmp/ansible  
  
RUN echo "===> Installing Docker" \  
&& apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https \  
ca-certificates \  
\  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" >
/etc/apt/sources.list.d/docker.list \  
\  
&& apt-get update && apt-get install -y \  
docker-engine \  
\  
&& curl -L https://github.com/docker/compose/releases/download/1.11.2/docker-
compose-$(uname -s)-$(uname -m) > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
\  
\  
&& echo "===> Adding PHP7" \  
\  
\  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C \  
&& echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" >
/etc/apt/sources.list.d/php.list \  
\  
&& apt-get update \  
&& apt-get purge -y --auto-remove php5-* php-* \  
&& apt-get install -y --no-install-recommends \  
php7.0-bz2 \  
php7.0-cli \  
php7.0-curl \  
php7.0-fpm \  
php7.0-gd \  
php7.0-gmp \  
php7.0-intl \  
php7.0-json \  
php7.0-mbstring \  
php7.0-mysql \  
php7.0-opcache \  
php7.0-pgsql \  
php7.0-sqlite3 \  
php7.0-xml \  
php7.0-zip \  
\  
php-amqp \  
php-apcu \  
php-apcu-bc \  
php-bcmath \  
php-geoip \  
php-igbinary \  
php-imagick \  
php-memcached \  
php-mongodb \  
php-msgpack \  
php-redis \  
php-ssh2 \  
php-uploadprogress \  
php-uuid \  
php-yaml \  
php-zmq \  
\  
&& apt-get purge -y --auto-remove $(dpkg -l | grep ii | grep php7.1 | awk
'{print $2}') \  
\  
&& apt-get purge -y --auto-remove \  
apache2-bin \  
autoconf \  
automake \  
autotools-dev \  
binutils \  
cpp \  
gcc \  
php-dev \  
\  
&& echo "====Fixing links====" \  
\  
&& ls -Rl /etc/php* \  
\  
&& rm -vrf /etc/php/5* \  
&& rm -vrf /etc/php/7.0/apache* \  
\  
&& cp -vrf /etc/php/7.0/* /etc/php/ \  
\  
&& rm -vrf /etc/php/7.0/* \  
&& rm -vrf /etc/php/7.1/* \  
\  
&& cp -vrf /etc/php/fpm/conf.d /etc/php/conf.d \  
&& ln -vs /etc/php/mods-available /etc/php/7.0/mods-available \  
&& ln -vs /etc/php/fpm /etc/php/7.0/fpm \  
&& ln -vs /etc/php/cli /etc/php/7.0/cli \  
&& rm -vrf /etc/php/fpm/conf.d \  
&& ln -vs /etc/php/conf.d /etc/php/fpm/conf.d \  
&& rm -vrf /etc/php/cli/conf.d \  
&& ln -vs /etc/php/conf.d /etc/php/cli/conf.d \  
\  
&& ln -vs /usr/sbin/php-fpm7.0 /usr/local/sbin/php-fpm \  
\  
&& mkdir -p /etc/php/conf.d.dist/ \  
&& cp -vrf /etc/php/conf.d/*.ini /etc/php/conf.d.dist/ \  
\  
&& ls -Rl /etc/php* \  
\  
&& echo "=== check php and install tools ===" \  
\  
&& php -v \  
&& php -m \  
&& php --ini \  
\  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer --version \  
\  
&& composer global require --prefer-source --no-interaction jakub-onderka/php-
parallel-lint \  
\  
&& wget https://phar.phpunit.de/phpunit.phar && chmod +x phpunit.phar && mv
phpunit.phar /usr/local/bin/phpunit \  
&& phpunit --version \  
\  
\  
&& echo "===> Adding Ansible" \  
\  
\  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 7BB9C367
\  
&& echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" |
tee /etc/apt/sources.list.d/ansible.list \  
&& apt-get -y update && apt-get install -y --no-install-recommends \  
ansible \  
\  
&& echo "===> Adding ansible hosts" \  
&& echo '[local]\nlocalhost\n' > /etc/ansible/hosts \  
\  
\  
&& echo "===> Cleanup" \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
&& rm -rf /usr/{lib,lib/share,share}/{man,doc,info,gnome/help,cracklib} \  
&& rm -rf /usr/{lib,lib64}/gconv \  
\  
&& echo "===> Done"  
  
COPY docker /  
  
# && echo "===> Installing ansible roles" \  
# && ansible-galaxy install -ir /tmp/ansible/requirements.txt \  
# \  
# && echo "===> Run ansible playbook" \  
# && ls -lr /tmp/ansible \  
# && ansible-playbook --version \  
# && ansible-playbook -vv -i "localhost," -c local /tmp/ansible/main.yml \  
  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 5.9.1  
ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules  
# Set up our PATH correctly so we don't have to long-reference npm, node, &c.  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
# Install nvm with node and npm  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default \  
&& npm -g install \  
casperjs \  
phantomjs \  
\  
&& echo "===> Done"  

