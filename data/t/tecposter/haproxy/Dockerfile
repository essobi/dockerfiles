FROM tecposter/ubuntu:latest  
  
MAINTAINER "zhanjh@126.com"  
# ref. https://hub.docker.com/_/haproxy/  
# ref. https://store.docker.com/images/85c386ff-85a7-4d61-b309-5901f625c36f  
# curl -SL "http://www.haproxy.org/download/1.6/src/haproxy-1.6.9.tar.gz" -o
haproxy.tar.gz \  
  
COPY haproxy-1.6.9.tar.gz /usr/local/src/haproxy.tar.gz  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get upgrade --no-install-recommends --no-install-suggests -y \  
  
&& build_deps="gcc make build-essential libc6-dev libpcre3-dev libssl-dev" \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
$build_deps \  
  
&& mkdir -p /usr/local/src/haproxy \  
&& tar -zxf /usr/local/src/haproxy.tar.gz -C /usr/local/src/haproxy --strip-
components=1 \  
  
&& make -C /usr/local/src/haproxy \  
TARGET=linux2628 \  
USE_PCRE=1 PCREDIR= \  
USE_OPENSSL=1 \  
USE_ZLIB=1 \  
CPU=native \  
all \  
install-bin \  
  
&& rm -rf /usr/local/src/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove $build_deps  

