FROM tecposter/ubuntu:latest  
  
MAINTAINER "zhanjh@126.com"  
# ref. https://hub.docker.com/_/redis/  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get upgrade --no-install-recommends --no-install-suggests -y \  
  
&& build_deps="gcc make build-essential curl" \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
$build_deps \  
  
&& cd /usr/local/src/ \  
&& curl -SL "http://download.redis.io/redis-stable.tar.gz" -o redis-
stable.tar.gz \  
&& tar -zxf redis-stable.tar.gz \  
&& cd redis-stable \  
  
&& make \  
&& cd src \  
&& make install \  
  
&& cd / \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/local/src/* \  
&& apt-get purge -y --auto-remove $build_deps  

