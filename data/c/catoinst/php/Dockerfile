# Basic apache php 7.0 appserver for Lando  
#  
# docker build -t catoinst/php:7.0-apache .  
  
FROM devwithlando/php:7.0-apache  
  
# Install dependencies we need  
RUN apt-get update && apt-get install -y \  
libxslt-dev \  
libssh2-1-dev \  
libtidy-dev \  
vim \  
build-essential \  
chrpath \  
libxft-dev \  
python-pip \  
libyaml-0-2 \  
python-yaml \  
python-dev \  
python-pandas \  
parallel \  
&& docker-php-ext-install \  
xsl \  
tidy \  
&& yes '' | pecl install ssh2-1.1.2 \  
&& cd / \  
&& git clone -b feature/php7 https://github.com/sqmk/pecl-jsmin.git \  
&& cd pecl-jsmin \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& cd / \  
&& git clone https://github.com/php/pecl-php-uploadprogress.git \  
&& cd pecl-php-uploadprogress \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& cd / \  
&& git clone https://github.com/igbinary/igbinary.git \  
&& cd igbinary \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& docker-php-ext-enable \  
ssh2 \  
jsmin \  
uploadprogress \  
igbinary \  
&& pip install boto3 --upgrade \  
&& pip install awscli \  
&& a2enmod expires headers \  
&& apt-get -y clean \  
&& apt-get -y autoclean \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/apt/lists/* && rm -rf && rm -rf /var/lib/cache/* && rm -rf
/var/lib/log/* && rm -rf /tmp/* \  
&& ulimit –f unlimited  

