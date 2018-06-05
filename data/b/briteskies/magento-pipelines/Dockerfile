# Generic Docker Configuration  
FROM php:7.0-cli  
LABEL maintainer="Sam.Rogal@briteskies.com"  
  
# Install Basic Magento Requirements  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update  
&& apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev \  
libicu-dev \  
git \  
default-jre \  
&& docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install \  
bcmath \  
#curl \ #already loaded  
gd \  
intl \  
#mbstring \ #already loaded  
mcrypt \  
#hash \ #already loaded  
#simplexml \ #already loaded  
#pdo \ #already loaded  
pdo_mysql \  
soap \  
#xml \ #already loaded  
xsl \  
#json \ #already loaded  
#iconv #already loaded  
zip \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
# Add ElasticSearch 2.4.6  
RUN curl -o elasticsearch-2.4.6.deb
https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/2.4.6/elasticsearch-2.4.6.deb
\  
&& dpkg -i elasticsearch-2.4.6.deb \  
&& rm elasticsearch-2.4.6.deb \  
&& systemctl enable elasticsearch.service \  
&& /usr/share/elasticsearch/bin/plugin install analysis-phonetic \  
&& /usr/share/elasticsearch/bin/plugin install analysis-icu \  
&& echo "script.inline: on" >> /etc/elasticsearch/elasticsearch.yml \  
&& echo "script.indexed: on" >> /etc/elasticsearch/elasticsearch.yml  
  
# Install ioncube loader  
RUN curl -o ioncube.tar.gz
http://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
\  
&& tar -xzvf ioncube.tar.gz \  
&& mv ioncube/ioncube_loader_lin_7.0.so /usr/local/lib/php/extensions/* \  
&& rm -rf ioncube.tar.gz ioncube  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install Composer Modules  
RUN composer global require hirak/prestissimo \  
&& composer global require deployer/deployer \  
&& ln -s /root/.composer/vendor/bin/dep /usr/local/bin/dep \  
&& ln -s /usr/local/bin/dep /usr/local/bin/deployer  
  
# Copy Configuration Files  
ADD context/php.ini /usr/local/etc/php/  
ADD context/ioncube.ini /usr/local/etc/php/conf.d/00-ioncube.ini  
ADD context/docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
WORKDIR /srv/www  

