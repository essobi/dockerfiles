FROM debian:jessie  
  
MAINTAINER Chris Kanich <kaytwo@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
traceroute \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/sbin/traceroute"]  

