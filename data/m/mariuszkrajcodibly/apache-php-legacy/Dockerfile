FROM debian:jessie  
  
ENV ALLOW_OVERRIDE **False**  
ENV TERM xterm  
  
# Update packages list  
# Install Apache & PHP  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y --force-yes \  
git curl nano wget vim make \  
apache2 libapache2-mod-php5 \  
php5-common php5-cli php5-fpm php-pear php5-dev php5-xdebug \  
php5-mcrypt php5-mysql php5-apcu \  
php5-gd php5-imagick php5-curl php5-intl \  
php5-redis php5-sqlite php5-pgsql php5-memcached \  
ca-certificates libcurl3-openssl-dev libssh2-php pkg-config;  
  
# CMAKE 3.5.2 instead of jessie's 3.0.2  
RUN wget https://cmake.org/files/v3.5/cmake-3.5.2-Linux-x86_64.sh \  
&& sh cmake-3.5.2-Linux-x86_64.sh --skip-license  
  
# AMQP  
# Mongo  
RUN git clone git://github.com/alanxz/rabbitmq-c.git \  
&& mkdir /rabbitmq-c/build \  
&& cd /rabbitmq-c/build && cmake -DCMAKE_INSTALL_PREFIX=/usr/local .. \  
&& cd /rabbitmq-c/build && cmake --build . --target install \  
&& ln -s /usr/local/lib/x86_64-linux-gnu/librabbitmq.so
/usr/local/lib/librabbitmq.so \  
&& ln -s /usr/local/lib/x86_64-linux-gnu/librabbitmq.so.4
/usr/local/lib/librabbitmq.so.4 \  
&& printf "\n" | pecl install amqp \  
&& printf "\n" | pecl install mongo \  
&& echo 'extension=mongo.so' >> /etc/php5/cli/conf.d/20-mongo.ini \  
&& echo 'extension=mongo.so' >> /etc/php5/fpm/conf.d/20-mongo.ini \  
&& echo 'extension=mongo.so' >> /etc/php5/apache2/conf.d/20-mongo.ini \  
&& echo 'extension=amqp.so' >> /etc/php5/cli/conf.d/20-amqp.ini \  
&& echo 'extension=amqp.so' >> /etc/php5/fpm/conf.d/20-amqp.ini \  
&& echo 'extension=amqp.so' >> /etc/php5/apache2/conf.d/20-amqp.ini \  
  
COPY config/memory-limit.ini /etc/php5/cli/conf.d/memory-limit.ini  
COPY config/memory-limit.ini /etc/php5/fpm/conf.d/memory-limit.ini  
COPY config/memory-limit.ini /etc/php5/apache2/conf.d/memory-limit.ini  
  
COPY config/xdebug.ini /etc/php5/cli/conf.d/xdebug.ini  
COPY config/xdebug.ini /etc/php5/fpm/conf.d/xdebug.ini  
COPY config/xdebug.ini /etc/php5/apache2/conf.d/xdebug.ini  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Phing  
RUN wget http://www.phing.info/get/phing-latest.phar \  
&& mv phing-latest.phar /usr/local/bin/phing \  
&& chmod +x /usr/local/bin/phing  
  
# PHP CS  
RUN wget https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \  
&& mv phpcs.phar /usr/local/bin/phpcs \  
&& chmod +x /usr/local/bin/phpcs  
  
# Node.js & Npm & phantomjs  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - \  
&& apt-get install --no-install-recommends -y nodejs bzip2 \  
&& npm install --global phantomjs-prebuilt  
  
# Apache configuration  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf \  
&& sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini \  
&& sed -i "s/expose_php.*/expose_php = \"off\"/g" /etc/php5/apache2/php.ini \  
&& mkdir -p /etc/apache2/ssl \  
&& openssl req \  
-new \  
-newkey rsa:4096 \  
-days 365 \  
-nodes \  
-x509 \  
-subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=local.kiwibem.com" \  
-keyout /etc/apache2/ssl/apache.key \  
-out /etc/apache2/ssl/apache.crt \  
&& /usr/sbin/php5enmod mcrypt \  
&& a2enmod rewrite \  
&& a2enmod php5 \  
&& a2enmod ssl \  
&& rm -rf /etc/apache2/sites-enabled/000-default.conf  
  
COPY config/bashrc /root/.bashrc  
  
# Copy image configuration and scripts  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
EXPOSE 80 3306 27017  
CMD ["/run.sh"]  

