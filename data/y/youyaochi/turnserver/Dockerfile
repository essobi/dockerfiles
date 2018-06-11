FROM phusion/baseimage:0.9.22  
MAINTAINER Brian Prodoehl <bprodoehl@connectify.me>  
  
# Set correct environment variables.  
ENV HOME /root  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN apt-get update && apt-get install -y --no-install-recommends
coturn=4.5.0.3-1build1 && rm -rf /var/lib/apt/lists/*  
  
ENV COTURN_VER 4.5.0.3  
RUN mkdir /etc/service/turnutils_peer  
COPY turnutils_peer.sh /etc/service/turnutils_peer/run  
  
RUN mkdir /etc/service/turnserver  
COPY turnserver.sh /etc/service/turnserver/run  

