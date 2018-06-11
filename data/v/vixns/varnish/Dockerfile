FROM debian:jessie-backports  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update && apt-get install -y \--no-install-recommends apt-
transport-https git curl ca-certificates \  
&& curl -s https://repo.varnish-cache.org/GPG-key.txt | apt-key add \- \  
&& echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.1" | \  
tee -a /etc/apt/sources.list.d/varnish-cache.list \  
&& mkdir /src \  
&& cd /src \  
&& apt-get update \  
&& apt-get -y \--no-install-recommends install \  
varnish varnish-dev build-essential automake libtool python-docutils \  
&& git clone https://github.com/nigoroll/libvmod-dynamic.git \  
&& cd /src/libvmod-dynamic \  
&& ./autogen.sh \  
&& ./configure \  
&& make install \  
&& dpkg --purge varnish-dev build-essential automake libtool python-docutils \  
&& apt-get -y autoremove \  
&& cd / && rm -rf /var/lib/apt/lists/* /src  
  
ENV VCL_CONFIG=/etc/varnish/default.vcl \  
STORAGE_BACKEND=malloc \  
CACHE_SIZE=64m \  
TELNET_PORT=6082 \  
LISTEN_PORT=6086 \  
VARNISHD_PARAMS="-p default_ttl=3600 -p default_grace=3600"  
  
COPY start.sh /start.sh  
CMD ["/start.sh"]  

