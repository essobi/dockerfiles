FROM ubuntu:16.04  
MAINTAINER Marco Antonio Martins Junior <somatorio@gmail.com>  
RUN apt-get update && apt-get install -y xfce4-screenshooter-plugin --no-
install-recommends && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["xfce4-screenshooter"]  

