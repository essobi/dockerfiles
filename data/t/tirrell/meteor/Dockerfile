FROM debian:stretch-slim  
  
RUN apt-get update && \  
apt-get install curl sudo -y && \  
useradd -c 'Meteor user' -m -d /home/meteor -s /bin/bash meteor && \  
apt-get clean && \  
echo "\nmeteor ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
rm -Rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /home/meteor  
  
USER meteor  
  
COPY install.sh install.sh  
  
RUN ./install.sh  
  
ENV PATH "$PATH:/home/meteor/.meteor"  

