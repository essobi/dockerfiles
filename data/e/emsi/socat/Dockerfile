FROM debian:wheezy  
  
RUN deps=' \  
socat \  
'; \  
set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends $deps \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 80  

