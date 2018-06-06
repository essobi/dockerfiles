FROM debian:stable-slim  
  
ADD
https://media.codeweavers.com/pub/crossover/cxlinux/demo/crossover_16.2.5-1.deb
/crossover_16.2.5-1.deb  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y \--no-install-recommends sudo python python-dbus python-
gtk2 && \  
useradd -ms /bin/bash -G sudo crossover && \  
passwd -d crossover && \  
(dpkg -i /crossover_16.2.5-1.deb 2>/dev/null || apt-get install -f -y \--no-
install-recommends) && \  
rm -rf /crossover_16.2.5-1.deb /var/lib/apt/lists/*  
  
USER crossover  
WORKDIR /home/crossover  
ENV HOME /home/crossover

