FROM bezrukovp/php-fpm:7.1  
  
MAINTAINER Pavel Bezrukov <bezrukov.ps@gmail.com>  
  
ENV PHALCON_VERSION=3.1.2  
  
RUN \  
# Install dev dependencies  
apk --no-cache add --virtual build-dependencies \  
autoconf \  
g++ \  
file \  
re2c \  
make \  
# Install latest Phalcon  
&& curl -sS -o /tmp/phalcon.tar.gz
https://codeload.github.com/phalcon/cphalcon/tar.gz/v${PHALCON_VERSION} \  
&& cd /tmp/ \  
&& tar xvzf phalcon.tar.gz \  
&& cd cphalcon-${PHALCON_VERSION}/build \  
&& sh install \  
&& echo "extension=phalcon.so" > /usr/local/etc/php/conf.d/50-phalcon.ini \  
# Cleanup  
&& apk del build-dependencies \  
&& rm -rf cphalcon-${PHALCON_VERSION} \  
v${PHALCON_VERSION} \  
/var/cache/apk/* \  
/tmp/* \  
# Remove unneeded envirnment vars  
&& unset PHALCON_VERSION

