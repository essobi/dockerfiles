FROM radmas/iyc-extra-deps  
  
MAINTAINER fernando.moro@radmas.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#################################################  
# SUDO  
  
RUN \  
apt-get update && \  
apt-get -y install \  
sudo && \  
rm -rf /var/lib/apt/lists/*  
  
#################################################  
# RADMAS USER  
  
RUN \  
sudo useradd radmas --shell /bin/bash --create-home && \  
sudo usermod -a -G sudo radmas && \  
echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers && \  
echo 'radmas:d0ck3r' | chpasswd  
  
#################################################  
  
USER radmas  
  
CMD ["sudo", "/usr/bin/supervisord"]  

