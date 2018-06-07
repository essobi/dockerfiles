FROM inklabs/php-fpm:7.1  
  
LABEL maintainer="Jamie Isaacs <pdt256@gmail.com>"  
  
WORKDIR /usr/local/src  
  
ENV PHALCON_URL="https://github.com/phalcon/cphalcon/archive/v3.2.2.tar.gz" \  
RE2C_URL="https://github.com/skvadrik/re2c/releases/download/0.16/re2c-0.16.tar.gz"
\  
BUILD_DEPENDENCIES="\  
gcc \  
gcc-c++ \  
git \  
make \  
autoconf \  
pcre-devel \  
wget"  
  
USER root  
  
RUN yum -y update \  
&& yum -y install $BUILD_DEPENDENCIES \  
\  
&& wget -q $RE2C_URL -O re2c.tgz \  
&& mkdir /usr/local/src/re2c \  
&& tar zxf re2c.tgz -C /usr/local/src/re2c \--strip-components=1 \  
&& ( \  
cd /usr/local/src/re2c \  
&& ./configure \  
&& make \  
&& make install \  
) \  
&& rm re2c.tgz \  
&& wget -q $PHALCON_URL -O phalcon.tgz \  
&& mkdir /usr/local/src/phalcon \  
&& tar zxf phalcon.tgz -C /usr/local/src/phalcon \--strip-components=1 \  
&& ( \  
cd /usr/local/src/phalcon/build \  
&& ./install \  
) \  
&& rm phalcon.tgz \  
&& yum -y remove $BUILD_DEPENDENCIES \  
&& yum clean all  
  
COPY ./phalcon.ini /usr/local/etc/php/conf.d/phalcon.ini  
  
EXPOSE 9000  
CMD ["php-fpm"]  
USER www-data  

