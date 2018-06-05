FROM debian:jessie  
  
MAINTAINER YuLun SHih <shih@yulun.me>  
  
ADD assets /assets  
  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install curl dnsmasq \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 53/tcp  
EXPOSE 53/udp  
  
CMD /assets/scripts/start.sh  

