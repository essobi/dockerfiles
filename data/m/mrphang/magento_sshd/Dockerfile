FROM rastasheep/ubuntu-sshd  
MAINTAINER Michael A. Phang <mphangdev@gmail.com>  
  
COPY install /usr/local/bin/install_magento  
RUN apt-get -qqy update  
RUN apt-get -qqy install git \  
libmcrypt-dev \  
libpng12-dev \  
libxml2-dev \  
graphviz \  
libxml2-utils \  
libxslt-dev \  
mysql-client \  
vim \  
xz-utils \  
php5-dev \  
php5-cli \  
php5-curl \  
php-pear \  
php5-mysql \  
curl \  
&& pecl install -o -f xdebug \  
# simple init subsystem to help prevent zombie processes  
&& curl -L -o /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.0.1/dumb-init_1.0.1_amd64 \  
&& curl -L -o /usr/local/bin/jq
https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 \  
&& chmod +x /usr/local/bin/dumb-init \  
&& useradd -m -s /bin/bash mage \  
&& echo "mage:mage" | chpasswd \  
&& usermod -aG mage www-data \  
# Idiopathic rm failure; loop is workaround  
&& until rm -rf /tmp/pear /var/lib/apt/lists; do sleep 1; done  
  
##  
# Install useful developer tools  
# including bootstrap installing Composer  
COPY composer.* /home/mage/.composer/  
WORKDIR /home/mage  
ENV COMPOSER_HOME=/home/mage/.composer/  
RUN curl -OSs https://getcomposer.org/composer.phar \  
&& php composer.phar global install \  
\--no-ansi \  
\--no-interaction \  
\--no-progress \  
\--optimize-autoloader \  
\--prefer-dist \  
&& php composer.phar clear-cache \  
&& rm composer.phar \  
&& chown -R mage:mage /home/mage  
  
RUN echo "export PATH=\$PATH:\$HOME/.composer/vendor/bin" >>
/home/mage/.bashrc \  
&& echo "cd /srv/magento" >> /home/mage/.bashrc  
CMD ["/usr/sbin/sshd", "-D"]  
ENTRYPOINT ["dumb-init"]  

