FROM ubuntu:16.04  
MAINTAINER Liang Shi <jeremy@pda.sh>  
  
RUN apt-get update && \  
apt-get install -y language-pack-en-base && \  
export LC_ALL=en_US.UTF-8 && \  
export LANG=en_US.UTF-8 && \  
apt-get install -y build-essential apt-transport-https \  
git \  
curl \  
wget \  
vim \  
pkg-config libssl-dev \  
libmariadbd-dev \  
software-properties-common \  
python-software-properties && \  
apt-get update && \  
apt-add-repository -y ppa:ondrej/php  
  
#install php 7 and package  
RUN apt-get update && apt-get install -y php7.1 \  
php7.1-bcmath \  
php7.1-curl \  
php7.1-sqlite3 \  
php7.1-dev \  
php7.1-mbstring  
  
# install latest libevent  
RUN wget -c
https://github.com/libevent/libevent/releases/download/release-2.1.8-stable/libevent-2.1.8-stable.tar.gz
-P /usr/local/src && \  
cd /usr/local/src && \  
tar -zxvf libevent-2.1.8-stable.tar.gz && \  
cd libevent-2.1.8-stable && \  
./configure --prefix=/usr/local/libevent-2.1.8-stable && \  
make && make install  
  
# install event module  
RUN wget -c http://pecl.php.net/get/event-2.3.0.tgz -P /usr/local/src && \  
cd /usr/local/src && \  
tar -zxvf event-2.3.0.tgz && cd event-2.3.0 && \  
$(which phpize) && \  
./configure --with-event-libevent-dir=/usr/local/libevent-2.1.8-stable/ && \  
make && make install && \  
touch /etc/php/7.1/cli/conf.d/20-event.ini && \  
echo 'extension=event.so' >> /etc/php/7.1/cli/conf.d/20-event.ini  
  
# install ds module  
RUN cd /tmp && git clone https://github.com/php-ds/extension "php-ds" && \  
cd php-ds && \  
$(which phpize) && \  
./configure && \  
make && make install && \  
touch /etc/php/7.1/cli/conf.d/30-ds.ini && \  
echo 'extension=ds.so' >> /etc/php/7.1/cli/conf.d/30-ds.ini  
  
# install php composer  
RUN curl -s https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
# install xidells  
RUN wget
https://sourceforge.net/projects/videlibri/files/Xidel/Xidel%200.9.6/xidel-0.9.6.linux64.tar.gz/download
&& \  
# cd /tmp  
mv download xidel.tar.gz &&\  
tar -zxvf xidel.tar.gz &&\  
mv xidel /usr/local/bin  

