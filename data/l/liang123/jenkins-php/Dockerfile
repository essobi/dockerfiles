# Official images are cool.  
FROM jenkins  
  
# Jenkins is using jenkins user, we need root to install things.  
USER root  
  
# Install php packages.  
RUN apt-get update && apt-get install -y \  
php5-cli \  
php5-dev \  
php5-curl \  
curl \  
php-pear \  
rsync \  
ant  
  
# Install php xdebug extension for code coverage  
# Setup the Xdebug version to install  
ENV XDEBUG_VERSION 2.4.1  
ENV XDEBUG_SHA1 52b5cede5dcb815de469d671bfdc626aec8adee3  
  
# Install Xdebug  
RUN set -x \  
&& curl -SL "http://www.xdebug.org/files/xdebug-$XDEBUG_VERSION.tgz" -o
xdebug.tgz \  
&& echo $XDEBUG_SHA1 xdebug.tgz | sha1sum -c - \  
&& mkdir -p /usr/src/xdebug \  
&& tar -xf xdebug.tgz -C /usr/src/xdebug --strip-components=1 \  
&& rm xdebug.* \  
&& cd /usr/src/xdebug \  
&& phpize \  
&& ./configure \  
&& make -j"$(nproc)" \  
&& make install \  
&& make clean  
  
#COPY ext-xdebug.ini /etc/php5/mods-available/  
#COPY ext-xdebug.ini /etc/php5/cli/conf.d/  
# install phpunit  
RUN curl -L https://phar.phpunit.de/phpunit.phar -o /usr/local/bin/phpunit \  
&& chmod a+x /usr/local/bin/phpunit  
  
# Install nodejs  
ENV NODEJS_VERSION 6.3.1  
ENV NODEJS_SHA256
eccc530696d18b07c5785e317b2babbea9c1dd14dbab80be734b820fc241ddea  
  
RUN set -x \  
&& curl -SL https://nodejs.org/dist/v$NODEJS_VERSION/node-v$NODEJS_VERSION-
linux-x64.tar.gz -o node.tar.gz \  
&& echo $NODEJS_SHA256 node.tar.gz | sha256sum -c - \  
&& mkdir /nodejs \  
&& tar xvzf node.tar.gz -C /nodejs --strip-components=1  
  
ENV PATH $PATH:/nodejs/bin  
  
#The official Debian and Ubuntu images automatically run apt-get clean, so
explicit invocation is not required.  
#RUN apt-get clean -y  
# Go back to jenkins user.  
USER jenkins  

