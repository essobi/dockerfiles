FROM debian:8  
MAINTAINER Fabien Evain fabien.evain@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq && apt-get install -qq \  
curl \  
libedit2 \  
libjemalloc1 \  
build-essential \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV VARNISH_VERSION 5.0.0  
RUN curl -J -L -s -k \  
"https://repo.varnish-
cache.org/pkg/${VARNISH_VERSION}/varnish_${VARNISH_VERSION}-1_amd64.deb" \  
-o /tmp/varnish.deb \  
&& dpkg -i /tmp/varnish.deb \  
&& rm /tmp/varnish.deb  
  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV CACHE_SIZE 64m  
ENV VARNISHD_PARAMS -p default_ttl=3600 -p default_grace=3600  
COPY varnish-daemon /usr/local/bin/  
  
EXPOSE 80  
CMD ["varnish-daemon"]

