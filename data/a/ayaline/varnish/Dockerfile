FROM debian:jessie  
MAINTAINER pborreli <pascal@borreli.com>  
  
RUN apt-get update && apt-get install -y curl apt-transport-https \  
&& curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add \- \  
&& echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.0" >>
/etc/apt/sources.list.d/varnish-cache.list \  
&& apt-get update \  
&& apt-get install -y varnish libvarnishapi-dev libcurl3-dev git build-
essential automake autoconf libtool pkg-config python-docutils \  
&& git clone https://github.com/varnish/libvmod-curl.git \  
&& cd libvmod-curl/ \  
&& git checkout 4.0 \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf /var/lib/apt/lists/*  
  
  
  

