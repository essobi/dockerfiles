FROM bezrukovp/workspace-php:7.0  
MAINTAINER Pavel Bezrukov, https://bezr.pro  
  
ENV PHP_VERSION=7.0  
ENV PHALCON_VERSION=3.1.2  
#  
#--------------------------------------------------------------------------  
# Software's Installation  
#--------------------------------------------------------------------------  
#  
# Install dev dependencies  
RUN mkdir -p /usr/local/etc/php/conf.d/ \  
&& cd /tmp \  
&& curl -sSLO
https://codeload.github.com/phalcon/cphalcon/tar.gz/v${PHALCON_VERSION} \  
&& tar xvzf v${PHALCON_VERSION} \  
&& cd cphalcon-${PHALCON_VERSION}/build \  
&& ./install \  
&& echo "extension=phalcon.so" > /etc/php/${PHP_VERSION}/mods-
available/phalcon.ini \  
&& ln -s /etc/php/${PHP_VERSION}/mods-available/phalcon.ini
/etc/php/${PHP_VERSION}/cli/conf.d \  
&& rm -rf /tmp/cphalcon-${PHALCON_VERSION}/build  

