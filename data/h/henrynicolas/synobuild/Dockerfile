FROM debian:jessie  
ARG
KERNEL_URL=https://sourceforge.net/projects/dsgpl/files/Synology%20NAS%20GPL%20Source/15152branch/avoton-
source/linux-3.10.x.txz/download  
  
RUN apt-get update && apt-get install -y \  
wget \  
build-essential \  
bc \  
libncurses5-dev  
  
RUN mkdir -p /opt/kernel/output  
  
RUN wget ${KERNEL_URL} -O /root/kernel.tar.gz  
RUN tar -xf /root/kernel.tar.gz -C /opt/kernel/  
  
VOLUME [ "/opt/kernel/output" ]  
  
CMD /bin/bash

