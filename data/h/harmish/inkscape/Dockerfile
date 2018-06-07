FROM ubuntu:16.04  
# install inkscape  
RUN apt update && \  
apt install -y software-properties-common && \  
add-apt-repository ppa:inkscape.dev/stable && \  
apt update && \  
apt install -y inkscape && \  
#  
# clean -up  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/workspace"]  
WORKDIR /workspace  

