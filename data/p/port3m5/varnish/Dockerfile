FROM debian:stretch  
  
MAINTAINER Anthony Porthouse <anthony@porthou.se>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y debian-archive-keyring \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils apt-transport-
https gnupg \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y curl \  
&& curl -sSf
"https://packagecloud.io/install/repositories/varnishcache/varnish5/config_file.list?os=debian&dist=stretch"
| tee /etc/apt/sources.list.d/varnish5.list \  
&& curl -L "https://packagecloud.io/varnishcache/varnish5/gpgkey" | apt-key
add - \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y varnish=5.2.0-1~stretch \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 6081  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV CACHE_SIZE 64m  
ENV VARNISHD_PARAMS -p default_ttl=3600 -p default_grace=3600  
ADD start.sh /usr/local/bin/start  
  
CMD ["bash", "/usr/local/bin/start"]  

