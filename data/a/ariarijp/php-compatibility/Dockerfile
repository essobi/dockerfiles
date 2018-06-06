FROM ubuntu:xenial  
MAINTAINER Takuya Arita <takuya.arita@gmail.com>  
  
RUN sed -i s/archive.ubuntu.com/ftp.jaist.ac.jp/ /etc/apt/sources.list && \  
apt-get update && \  
apt install -y php7.0-cli php7.0-xml curl git unzip && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
composer global require squizlabs/php_codesniffer && \  
curl -L -O https://github.com/wimg/PHPCompatibility/archive/master.zip && \  
unzip master.zip && \  
mv PHPCompatibility-master
~/.composer/vendor/squizlabs/php_codesniffer/CodeSniffer/Standards/PHPCompatibility
&& \  
rm master.zip && \  
apt remove -y curl git unzip && \  
apt autoremove -y  
ENV PATH $PATH:/root/.composer/vendor/bin  

