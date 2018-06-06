FROM debian:jessie  
  
RUN set -xe && \  
apt-get -qq update && \  
apt-get -qq install \  
curl \  
&& \  
apt-get clean && \  
rm -r /var/lib/apt/lists/* && \  
true  
  
ENTRYPOINT curl

