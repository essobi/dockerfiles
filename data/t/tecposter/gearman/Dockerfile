FROM tecposter/ubuntu:latest  
  
MAINTAINER "zhanjh@126.com"  
# http://gearman.org/getting-started/  
# https://github.com/gearman  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get upgrade -y --no-install-recommends --no-install-suggests \  
  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
libboost-all-dev gperf libevent-dev uuid-dev libcloog-ppl-dev \  
  
&& build_deps="gcc make build-essential curl ca-certificates" \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
$build_deps \  
  
&& cd /usr/local/src/ \  
&& curl -SL
"https://github.com/gearman/gearmand/releases/download/1.1.13/gearmand-1.1.13.tar.gz"
\  
-o gearmand-1.1.13.tar.gz \  
&& tar -zxf gearmand-1.1.13.tar.gz \  
&& cd gearmand-1.1.13/ \  
  
&& ./configure \  
&& make \  
&& make install \  
&& ldconfig \  
  
&& cd / \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/local/src/* \  
&& apt-get purge -y --auto-remove $build_deps  

