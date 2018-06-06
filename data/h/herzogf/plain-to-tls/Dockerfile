FROM debian:jessie-slim  
MAINTAINER Florian Herzog  
  
COPY . /  
  
RUN set -e && \  
apt-get update && apt-get install -y openssl stunnel && \  
rm -rf /var/lib/apt/lists/* && \  
chmod a+rx /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

