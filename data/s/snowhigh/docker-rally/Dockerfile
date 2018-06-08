FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y \  
git \  
vim && \  
apt-get clean  
  
RUN git clone -b stable/0.9 https://github.com/openstack/rally.git  
  
ADD admin-openrc.sh /rally/admin-openrc.sh  
  
RUN /rally/install_rally.sh -s -y  
  
WORKDIR /rally  

