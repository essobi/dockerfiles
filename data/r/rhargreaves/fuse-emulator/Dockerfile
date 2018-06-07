FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get -y install software-properties-common && \  
apt-add-repository multiverse && \  
apt-get update && \  
apt-get -y install fuse-emulator-common spectrum-roms fuse-emulator-utils  
  
ENTRYPOINT ["fuse"]  

