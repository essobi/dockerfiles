FROM debian:7.7  
MAINTAINER Max D. <lugamax@gmail.com>  
  
ADD ssh /root/.ssh  
  
RUN chmod 400 /root/.ssh/id_rsa \  
&& apt-get update && apt-get install -q -y \  
apt-utils vim software-properties-common python-software-properties \  
build-essential make cmake git curl wget openssh-client openssh-server  
  
RUN add-apt-repository 'deb http://http.debian.net/debian wheezy-backports
main' \  
&& apt-key adv --fetch-keys http://www.dotdeb.org/dotdeb.gpg \  
&& add-apt-repository 'deb http://packages.dotdeb.org wheezy all' \  
&& add-apt-repository 'deb http://packages.dotdeb.org wheezy-php55 all' \  
&& export DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -q -y \  
php5-dev=5.5.* php5-cli=5.5.* \  
php5-mongo php5-redis php5-mysql php5-sqlite php5-mcrypt php5-curl php5-imap
php-pear \  
&& git clone -b v0.5.2 git://github.com/alanxz/rabbitmq-c.git /tmp/rabbitmq-c
\  
&& mkdir /tmp/rabbitmq-c/build \  
&& mkdir -p /etc/php5/mods-available  
  
  
RUN cd /tmp/rabbitmq-c/build \  
&& cmake -DOPENSSL_LIBRARIES=/usr/local/ssl/lib \  
-DOPENSSL_ROOT_DIR=/usr/local/ssl -DCMAKE_INSTALL_PREFIX=/usr/local .. \  
&& cmake --build . --target install \  
&& ln -s /usr/local/lib/x86_64-linux-gnu/librabbitmq.so
/usr/local/lib/librabbitmq.so \  
&& ln -s /usr/local/lib/x86_64-linux-gnu/librabbitmq.so.1
/usr/local/lib/librabbitmq.so.1 \  
&& pecl install amqp \  
&& echo 'extension=amqp.so' >> /etc/php5/mods-available/amqp.ini \  
&& php5enmod amqp \  
&& php5enmod mcrypt \  
&& curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin --filename=composer \  
&& chmod a+x /usr/local/bin/composer  
  
RUN cd /root \  
&& /usr/bin/git clone git@github.com:ansible/ansible.git \  
&& cd ansible \  
&& /bin/bash -c "source ./hacking/env-setup -q" \  
&& apt-get install -q -y python2.7 python python-dev python-pip \  
&& pip install -q -U paramiko PyYAML Jinja2 httplib2 \  
&& git pull --rebase \  
&& git submodule update --init --recursive \  
&& make && make install  
  
USER 1000  

