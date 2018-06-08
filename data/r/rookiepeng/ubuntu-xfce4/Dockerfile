# DESCRIPTION: Xfce4 desktop on Ubuntu  
# AUTHOR: rookiepeng (https://zpeng.me)  
FROM ubuntu  
MAINTAINER rookiepeng  
  
RUN apt-get update && \  
apt-get -y --no-install-recommends install \  
xfce4 \  
xfce4-terminal \  
gvfs \  
breeze-cursor-theme \  
sudo  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN useradd -m -d /home/ubuntu -s /bin/bash ubuntu  
RUN echo "ubuntu:ubuntu" | chpasswd  
RUN usermod -aG sudo ubuntu  
  
USER ubuntu  
  
#ENV HOME /home/alpine  
ENTRYPOINT [ "startxfce4" ]

