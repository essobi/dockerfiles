FROM dialogtech/php7-nginx  
MAINTAINER Thomas Cooper <tom.cooper@dialogtech.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
ENV LANG C.UTF-8  
# install zephir, build and install Phalcon  
RUN apt-get update && \  
apt-get install -y --no-install-recommends php7.0-dev php7.0-mbstring re2c
make libpcre3-dev software-properties-common && \  
git clone git://github.com/phalcon/cphalcon.git && \  
git clone git://github.com/phalcon/zephir && \  
cd /zephir && \  
./install-nosudo && \  
cd /cphalcon && \  
git checkout 2.1.x && \  
~/bin/zephir build --backend=ZendEngine3 && \  
cp /cphalcon/ext/modules/phalcon.so /usr/lib/php/20151012/ && \  
apt-get remove --purge -y software-properties-common make && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_* && \  
cd / && \  
rm -rf /cphalcon && \  
rm -rf /zephir  
  
# Configure Phalcon and PHP  
RUN echo "extension=phalcon.so" > /etc/php/7.0/mods-available/phalcon.ini && \  
echo "extension=phalcon.so" > /etc/php/7.0/fpm/conf.d/21-phalcon.ini && \  
echo "extension=phalcon.so" > /etc/php/7.0/cli/conf.d/21-phalcon.ini  

