FROM ubuntu:latest  
  
MAINTAINER Hammad Ahmed <hammad@brokergenius.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update  
  
#  
#---------------------------------------------------  
# First Setting up locale to include utf8 charset  
#---------------------------------------------------  
#  
#  
#  
RUN apt-get install -y language-pack-en-base sudo  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ARG PUID=1000  
ARG PGID=1000  
RUN groupadd -g $PGID laradock && \  
useradd -u $PUID -g laradock -m laradock && \  
usermod -aG sudo laradock  
RUN sed -i.bkp -e \  
's/%sudo\s\\+ALL=(ALL\\(:ALL\\)\?)\s\\+ALL/%sudo ALL=NOPASSWD:ALL/g' \  
/etc/sudoers  
RUN apt-get update  
RUN apt-get install software-properties-common -y  
RUN add-apt-repository -y ppa:ondrej/php  
RUN add-apt-repository ppa:openjdk-r/ppa -y  
RUN apt-get update  
  
RUN apt-get -y install libxml2-utils php7.0 php-xdebug php7.0-gd php7.0-ldap \  
php7.0-sqlite php7.0-pgsql php-pear php7.0-mysql \  
php7.0-mcrypt php7.0-xmlrpc php7.0-cli php7.0-curl \  
php7.0-json php7.0-odbc php7.0-tidy php7.0-imap \  
php7.0-redis php7.0-intl php7.0-pgsql php7.0-mongodb \  
php7.0-sybase php7.0-zip php7.0-mbstring php7.0-bcmath php7.0-xml sendmail
supervisor \  
openjdk-7-jre\  
&& mkdir /run/php  
ENV PATH vendor/bin:$COMPOSER_HOME/vendor/bin:$PATH  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
  
  
# Installs Ant  
ENV ANT_VERSION 1.9.4  
RUN apt-get install -y wget curl git && cd ~ && \  
wget -q http://archive.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz && \  
tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \  
mv apache-ant-${ANT_VERSION} /opt/ant && \  
rm apache-ant-${ANT_VERSION}-bin.tar.gz  
ENV ANT_HOME /opt/ant  
ENV PATH ${PATH}:/opt/ant/bin  
  
  
  
ENV NODE_VERSION stable  
  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install nodejs -y  
RUN npm install bower -g && \  
npm install -g "gulpjs/gulp#4.0"  
  
# Install composer and add its bin to the PATH.  
RUN curl -s http://getcomposer.org/installer | php && \  
mv composer.phar /usr/bin/composer  
  
USER laradock  
  
#Installing php build packages  
RUN composer global require phpunit/phpunit && \  
composer global require phpunit/dbunit && \  
composer global require phing/phing && \  
composer global require "sebastian/phpcpd=*" && \  
composer global require phploc/phploc && \  
composer global require phpmd/phpmd && \  
composer global require squizlabs/php_codesniffer && \  
composer global require "codeception/codeception:*" && \  
echo 'export PATH="$PATH:$HOME/.composer/vendor/bin"' >> ~/.bashrc  
  
  
RUN . ~/.bashrc  
  
ENV COMPOSER_HOME /home/laradock/.composer  
ENV PATH vendor/bin:$COMPOSER_HOME/vendor/bin:$PATH  
  
WORKDIR /home/laradock  
RUN wget http://apigen.org/apigen.phar && \  
sudo chmod +x apigen.phar && \  
sudo mv apigen.phar /usr/local/bin/apigen  
  
COPY entrypoint.sh /  
RUN sudo chmod +x /entrypoint.sh  
  
ENV HOME_DIR /var/www/laravel  
ENV BUILD_USER laradock  
  
CMD ["/entrypoint.sh"]  

