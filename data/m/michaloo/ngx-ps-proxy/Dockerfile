FROM ubuntu:14.04  
WORKDIR /root  
ENV HOME /root  
  
RUN apt-get update && apt-get install -y \  
curl  
  
RUN curl -L https://github.com/michaloo/ngx_ps-
builder/releases/download/v0.0.1/nginx-1.6.2-1.9.32.2.tar.gz | \  
tar -xz --strip-components=1 -C /usr/local  
  
# install templater  
RUN curl -sL
https://github.com/michaloo/templater/releases/download/v0.0.1/templater.tar.gz
| \  
tar -xz -C /usr/local/bin  
  
VOLUME /var/ngx_pagespeed_cache  
VOLUME /var/log/pagespeed  
VOLUME /var/nginx_temp  
  
WORKDIR /ngx_ps-proxy  
ADD . /ngx_ps-proxy  
  
ENTRYPOINT ["/bin/bash"]  
CMD ["/ngx_ps-proxy/bin/start.sh"]  

