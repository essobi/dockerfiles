FROM debian:jessie  
  
LABEL maintainer "opsxcq@strm.sh"  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
git curl wget \  
qemu qemu-kvm qemu-system-x86 qemu-system \  
libvirt-bin libvirt-clients virtinst \  
cpio \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Setup virbr0  
COPY default-network.xml /etc/libvirt/qemu/networks/default.xml  
  
EXPOSE 5900  
VOLUME /iso  
  
VOLUME /src  
WORKDIR /src  
  
COPY main.sh /  

