FROM ubuntu:14.04.1  
MAINTAINER Tanmai Gopal <tanmaig@34cross.in>  
  
ENV NPS_VERSION 1.9.32.6  
ENV NGINX_VERSION 1.8.0  
ENV OPENSSL_VERSION 1.0.2d  
ENV BUILDDIR /b  
  
#Install the basic stuff  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get -y install wget unzip \  
&& apt-get -y install build-essential zlib1g-dev libpcre3 libpcre3-dev \  
&& mkdir ${BUILDDIR} && cd ${BUILDDIR} \  
&& wget
https://github.com/pagespeed/ngx_pagespeed/archive/release-${NPS_VERSION}-beta.zip
\  
&& unzip release-${NPS_VERSION}-beta.zip \  
&& cd ngx_pagespeed-release-${NPS_VERSION}-beta/ \  
&& wget https://dl.google.com/dl/page-speed/psol/${NPS_VERSION}.tar.gz \  
&& tar -xzvf ${NPS_VERSION}.tar.gz \  
&& cd ${BUILDDIR} \  
&& wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \  
&& tar -xvzf nginx-${NGINX_VERSION}.tar.gz \  
&& cd ${BUILDDIR} \  
&& wget http://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz \  
&& tar -xvzf openssl-${OPENSSL_VERSION}.tar.gz \  
&& cd ${BUILDDIR}/nginx-${NGINX_VERSION} \  
&& ./configure --add-module=${BUILDDIR}/ngx_pagespeed-
release-${NPS_VERSION}-beta/ --with-
openssl=${BUILDDIR}/openssl-${OPENSSL_VERSION} \--with-http_ssl_module --with-
http_realip_module \  
&& make && make install \  
&& cd / \  
&& rm -r ${BUILDDIR} \  
&& apt-get purge -y --auto-remove wget build-essential unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
#Redirect the screen outputs and stuff  
RUN ln -sf /dev/stdout /usr/local/nginx/logs/access.log  
RUN ln -sf /dev/stderr /usr/local/nginx/logs/error.log  
  
#Add /ngx_pagespeed_cache  
RUN mkdir /ngx_pagespeed_cache && chmod -R 777 /ngx_pagespeed_cache  
  
EXPOSE 80 443  
ENTRYPOINT ["/usr/local/nginx/sbin/nginx","-g","daemon off;"]  

