FROM debian:jessie  
MAINTAINER dan@typeamachines.com  
  
RUN apt-get update && apt-get install -y \  
debootstrap \  
qemu-user-static \  
qemu \  
git \  
sudo \  
time \  
xz-utils \  
dosfstools \  
kpartx \  
wget \  
parted \  
make  
  
COPY ./ /app  
WORKDIR /app  
VOLUME /app/deploy  
RUN scripts/install_dependencies.sh  

