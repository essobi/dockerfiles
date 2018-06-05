FROM debian:stretch-slim  
  
LABEL name="Varnish Cache" \  
version="6.0.0" \  
homepage="http://varnish-cache.org/" \  
maintainer="Christos Manios <maniopaido@gmail.com>"  
  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV CACHE_SIZE 64m  
ENV VARNISHD_PARAMS -p default_ttl=3600 -p default_grace=3600  
ENV VARNISH_VERSION 6.0.0  
COPY start.sh /usr/bin/start-varnish  
  
# Retrieve Varnish from  
#
https://packagecloud.io/varnishcache/varnish60/packages/debian/stretch/varnish_6.0.0-1~stretch_amd64.deb/download.deb  
RUN VARNISH_URL_VERSION="60" \  
&& apt-get update \  
&& apt-get install -y wget libjemalloc1 libncurses5 gcc libc6-dev \  
libc6.1-dev-alpha-cross libc-dev libedit2 libbsd0 \  
&& wget --content-disposition
https://packagecloud.io/varnishcache/varnish${VARNISH_URL_VERSION}/packages/debian/stretch/varnish_${VARNISH_VERSION}-1~stretch_amd64.deb/download.deb
\  
&& dpkg -i varnish_${VARNISH_VERSION}-1~stretch_amd64.deb \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -f varnish_${VARNISH_VERSION}-1~stretch_amd64.deb \  
&& mkdir -p "/orig/conf" \  
&& cp -Rp /etc/varnish/* /orig/conf \  
&& chmod 755 /usr/bin/start-varnish \  
&& update-rc.d -f varnish remove  
  
CMD ["start-varnish"]  
  
EXPOSE 6081

