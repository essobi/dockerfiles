FROM ubuntu:14.04  
  
MAINTAINER EnnWeb Cloud <cloud@ennweb.com>  
  
ENV \  
DEBIAN_FRONTEND=noninteractive \  
STORE_BACKEND=ceph \  
RABBIT_USER=openstack \  
RABBIT_PASS=rabbitpass \  
CONTROLLER_HOST=controller \  
REGION_NAME=RegionOne \  
NOVA_PASS=novapass \  
NEUTRON_PASS=neutronpass \  
METADATA_SECRET=metadatasecret \  
INTERFACE_NAME=eth1 \  
LISTEN_IP=0.0.0.0 \  
LOCAL_IP=10.0.0.1 \  
UUID=b3d14bb5-b523-4f24-aa56-0ab3fac96dc6  
  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y cloud-archive:liberty && \  
apt-get update && apt-get -y dist-upgrade && \  
apt-get install -y python-pymysql nova-compute sysfsutils neutron-plugin-
linuxbridge-agent conntrack ceph-common telnet curl && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
ADD entrypoint.sh /  
  
EXPOSE 5900 16509  
  
ENTRYPOINT ["/entrypoint.sh"]  

