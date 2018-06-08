FROM mamut3d/openstack_cli  
  
MAINTAINER Mamut3D  
  
LABEL Description="Openstack client tools with ansible client"  
  
RUN apt-get update && apt-get install -y software-properties-common && \  
apt-add-repository ppa:ansible/ansible && \  
apt-get update && apt-get install -y \  
ansible \  
qemu-utils \  
wget \  
curl \  
&& rm -rf /var/cache/apk/*  
  
CMD ["/bin/bash"]  

