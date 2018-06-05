FROM occitech/cakephp:5.6-fpm  
  
RUN apt-get update \  
&& apt-get install -y \  
locales \  
vim \  
lsof \  
curl \  
ca-certificates \  
nginx \  
python \  
python-pip \  
libmcrypt-dev \  
g++ \  
libicu-dev \  
&& cd /root \  
&& curl -L https://github.com/phpredis/phpredis/archive/2.2.7.tar.gz -o
phpredis.tar.gz \  
&& tar zxvf phpredis.tar.gz \  
&& rm -rf phpredis.tar.gz \  
&& mv phpredis* phpredis \  
&& cd phpredis \  
&& phpize \  
&& ./configure \  
&& make && make install \  
&& cd /root \  
&& rm -rf phpredis* \  
&& cd /root \  
&& curl -OL http://downloads.zend.com/guard/7.0.0/zend-loader-
php5.6-linux-x86_64.tar.gz \  
&& tar zxvf zend-loader-php5.6-linux-x86_64.tar.gz \  
&& cd zend-loader-php5.6-* \  
&& mkdir -p /usr/local/zend/ \  
&& cp ZendGuardLoader.so /usr/local/zend/ZendGuardLoader.so \  
&& cd /root \  
&& rm -rf zend-loader-php5.6-* \  
&& echo "zh_CN.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen \  
&& apt-get -y autoclean \  
&& apt-get -y clean \  
&& rm -rf /var/cache/apt/archives/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -f /etc/localtime \  
&& ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& pip install supervisor  
  
ENV LANG zh_CN.UTF-8  
ENV LC_ALL zh_CN.UTF-8  

