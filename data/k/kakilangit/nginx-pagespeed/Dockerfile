FROM debian:jessie  
MAINTAINER kakilangit <theguywhodrinkscoffeeandcodes@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && apt-get -y install \  
wget \  
build-essential \  
openssl \  
libssl-dev \  
zlib1g-dev \  
libpcre3 \  
libpcre3-dev \  
unzip \  
&& mkdir -p /tmp /var/log/nginx/  
  
# http://nginx.org/en/download.html  
ENV NGINX_VERSION 1.13.3  
# https://github.com/pagespeed/ngx_pagespeed/releases  
ENV NPS_VERSION 1.12.34.2  
ENV PS_NGX_EXTRA_FLAGS "--prefix=/etc/nginx --sbin-path=/usr/local/bin --conf-
path=/etc/nginx/conf/nginx.conf --error-log-path=/var/log/nginx/error.log
--http-log-path=/var/log/nginx/access.log --with-http_ssl_module --with-
http_realip_module --with-http_addition_module --with-http_sub_module --with-
http_dav_module --with-http_flv_module --with-http_mp4_module --with-
http_gunzip_module --with-http_gzip_static_module --with-
http_random_index_module --with-http_secure_link_module --with-
http_stub_status_module --with-http_auth_request_module --with-mail --with-
mail_ssl_module --with-file-aio --with-ipv6 --with-threads --with-stream
--with-stream_ssl_module --with-http_slice_module --with-http_v2_module"  
RUN cd /tmp && wget
https://github.com/pagespeed/ngx_pagespeed/archive/v${NPS_VERSION}-beta.zip \  
&& unzip v${NPS_VERSION}-beta.zip \  
&& cd ngx_pagespeed-${NPS_VERSION}-beta/ \  
&& wget https://dl.google.com/dl/page-speed/psol/${NPS_VERSION}-x64.tar.gz \  
&& tar -xzvf ${NPS_VERSION}-x64.tar.gz \  
&& rm -rf ${NPS_VERSION}-x64.tar.gz \  
&& cd /tmp \  
&& wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \  
&& tar -xvzf nginx-${NGINX_VERSION}.tar.gz  
  
RUN cd /tmp/nginx-${NGINX_VERSION}/ \  
&& ./configure ${PS_NGX_EXTRA_FLAGS} \--add-
module=/tmp/ngx_pagespeed-${NPS_VERSION}-beta \  
&& make && make install  
  
RUN apt-get purge -y wget build-essential libssl-dev zlib1g-dev libpcre3-dev
unzip \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /tmp/* && mkdir -p /var/ngx_pagespeed_cache && mkdir -p
/var/log/nginx/  
  
COPY ./conf /etc/nginx/conf  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

