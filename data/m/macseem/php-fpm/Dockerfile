FROM debian:7.7  
MAINTAINER Max D <lugamax@gmail.com>  
ADD ssh /root/.ssh  
ADD init/init.sh /init.sh  
RUN chmod 400 /root/.ssh/id_rsa \  
&& apt-get update \  
&& apt-get install -q -y software-properties-common python-software-properties
\  
&& add-apt-repository 'deb http://http.debian.net/debian wheezy-backports
main' \  
&& apt-key adv --fetch-keys http://www.dotdeb.org/dotdeb.gpg \  
&& add-apt-repository 'deb http://packages.dotdeb.org wheezy all' \  
&& add-apt-repository 'deb http://packages.dotdeb.org wheezy-php55 all' \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -q -y \  
php5-fpm=5.5.* php5-dev=5.5.* php5-cli=5.5.* \  
php5-mongo php5-redis php5-mysql php5-sqlite php5-mcrypt php5-curl php5-imap \  
supervisor git curl wget build-essential make cmake php-pear openssh-client
openssh-server \  
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
&& chmod a+x /usr/local/bin/composer \  
&& chmod a+x /init.sh  
  
ADD config/www.conf /etc/php5/fpm/pool.d/www.conf  

