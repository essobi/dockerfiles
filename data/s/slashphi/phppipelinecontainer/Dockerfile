FROM ubuntu:xenial  
MAINTAINER Michael Muenzing <michael.muenzing@gmail.com>  
  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#RUN apt-get -y -f install software-properties-common && \  
# add-apt-repository ppa:ondrej/php5-5.6 && \  
# apt-get update -y  
RUN apt-get update -y  
  
# PHP + extensions  
RUN apt-get -y -f --force-yes install php7.0-cli php7.0-dev php7.0-mysql
php7.0-xmlrpc php7.0-curl curl libicu-dev php7.0-sqlite php-memcached php-pear
php7.0-xsl php7.0-mcrypt php7.0-gd php7.0-intl php7.0-mbstring php7.0-bcmath
php7.0-zip php7.0-soap  
  
# PHP QA tools  
RUN apt-get install -y -f --force-yes ant sqlite3 git-core && \  
curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer && \  
# pear config-set auto_discover 1 && \  
# pear channel-discover pear.pdepend.org && \  
# pear channel-discover pear.phpmd.org && \  
# composer global require 'phploc/phploc=*' && \  
# pear install PHP_CodeSniffer && \  
# pear install pdepend/PHP_Depend && \  
# pear install --alldeps phpmd/PHP_PMD && \  
# composer global require "sebastian/phpcpd=*" && \  
# composer global require "theseer/phpdox=*" && \  
apt-get clean -y  
  
ENV PATH /root/.composer/vendor/bin:$PATH  
  
RUN apt-get update && \  
apt-get -y -f --force-yes install python-pip && \  
pip install awscli  
  
# PHP AWS Tools  
##RUN apt-get install -y -f --force-yes install unzip && \  
# curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && \  
# unzip awscli-bundle.zip && \  
# ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

