FROM ubuntu:14.04.4  
MAINTAINER Stephan Buys <stephan.buys@panoptix.co.za>  
ENV REFRESHED_ON "14 April 2016"  
RUN apt-get update && \  
apt-get install -y \  
curl \  
openssl  
  
WORKDIR /tmp  
RUN curl -OL
https://caddyserver.com/download/builds/161404115340998/caddy_linux_amd64_custom.tar.gz
&& \  
tar -xzf caddy_linux_amd64_custom.tar.gz && \  
mkdir -p /caddy && \  
cp /tmp/caddy /caddy/  
  
WORKDIR /caddy  
VOLUME ["/root/.caddy"]  
  
EXPOSE 80  
EXPOSE 443  
ENTRYPOINT ./caddy -agree  
  

