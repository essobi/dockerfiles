FROM ubuntu:17.10  
LABEL maintainer="Jared Harrington-Gibbs"  
LABEL description="A docker image that runs wireshark"  
  
ENV DISPLAY=":1.0"  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wireshark xvfb xrdp
tigervnc-standalone-server && \  
apt-get autoremove -y && \  
apt-get autoclean -y && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /var/run/xrdp/sockdir && \  
echo root:malware | chpasswd  
  
COPY startup.sh /  
  
#startup.sh contains  
##!/bin/bash  
#xrdp && \  
#xrdp-sesman && \  
#bash -c "Xvfb -nolisten tcp :1 -screen 0 800x600x16"  
ENTRYPOINT ["bash"]  
CMD ["startup.sh"]  

