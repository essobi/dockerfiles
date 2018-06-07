FROM ubuntu:14.04  
MAINTAINER Claudio Petrini <dod91@hotmail.it>  
# Forked from https://github.com/dgageot/ngxpagespeed (David Gageot
<david@gageot.net>)  
ENV DEBIAN_FRONTEND noninteractive  
ENV NGINX_VERSION 1.7.3  
# Install dependencies  
RUN apt-get update -qq  
RUN apt-get install -yqq build-essential zlib1g-dev libpcre3 libpcre3-dev
openssl libssl-dev libperl-dev wget zip ca-certificates  
  
# From instructions here: https://github.com/pagespeed/ngx_pagespeed  
# Download ngx_pagespeed  
# RUN cd /tmp && wget -q -O -
https://github.com/pagespeed/ngx_pagespeed/archive/v1.8.31.3-beta.tar.gz | tar
zxf -  
# RUN cd /tmp/ngx_pagespeed-1.8.31.3-beta/ && wget -q -O -
https://dl.google.com/dl/page-speed/psol/1.8.31.3.tar.gz | tar zxf -  
# In build --add-module=/tmp/ngx_pagespeed-1.8.31.3-beta  
# Download and build nginx  
RUN cd /tmp && wget -q -O -
http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz | tar zxf -  
RUN cd /tmp/nginx-${NGINX_VERSION} \  
&& ./configure --prefix=/etc/nginx/ --sbin-path=/usr/sbin/nginx --with-
http_ssl_module --with-http_spdy_module \  
&& make install  
  
# Cleanup  
#RUN rm -Rf /tmp/ngx_pagespeed-1.8.31.3-beta  
RUN rm -Rf /tmp/nginx-${NGINX_VERSION}  
  
EXPOSE 80  
EXPOSE 443  
VOLUME ["/etc/nginx/sites-enabled"]  
WORKDIR /etc/nginx/  
CMD ["/usr/sbin/nginx"]  
  
# Configure nginx  
COPY nginx.conf /etc/nginx/conf/nginx.conf  

