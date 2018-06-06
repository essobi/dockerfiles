FROM php:5.6-cli  
MAINTAINER fbrbovic@contained.cloud  
  
  
ENV ZEPHIRDIR /usr/share/zephir  
  
RUN apt-get update && \  
apt-get install -y git gcc make re2c php5 php5-json php5-dev libpcre3-dev sudo
&& \  
mkdir -p /usr/share/zephir && \  
git clone \--depth=1 -v https://github.com/phalcon/zephir /tmp/zephirinstall
&& \  
cd /tmp/zephirinstall && \  
./install -c && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/zephir"]  
WORKDIR /zephir  
  
ENTRYPOINT ["zephir"]  

