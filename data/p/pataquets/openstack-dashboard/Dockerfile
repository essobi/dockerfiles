FROM pataquets/apache:2.4  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
openstack-dashboard \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 80  

