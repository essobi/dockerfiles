FROM pataquets/ubuntu  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
beanstalkd \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 11300  

