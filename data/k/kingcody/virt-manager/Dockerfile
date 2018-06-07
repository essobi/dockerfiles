FROM debian:jessie  
MAINTAINER Cody Mize <me@codymize.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DISPLAY unix$DISPLAY  
RUN apt-get update && apt-get install -y \  
virt-manager \  
ssh \  
ssh-askpass-gnome && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["/usr/bin/virt-manager", "--no-fork"]  

