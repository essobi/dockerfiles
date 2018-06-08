FROM million12/centos-supervisor  
MAINTAINER Marcin Ryzycki marcin@m12.io, Przemyslaw Ozgo linux@ozgo.info  
  
RUN \  
yum update -y && \  
yum install -y epel-release && \  
yum remove -y fakesystemd && \  
yum install -y systemd wget bind-utils && \  
cd /tmp/ && \  
wget -l 1 -nd -nc -r -A.rpm
http://download.gluster.org/pub/gluster/glusterfs/3.6/3.6.2/EPEL.repo/epel-7/x86_64/
&& \  
yum install -y gluster* && \  
rm -f gluster* && \  
yum clean all  
  
COPY container-files /  
  
ENV GLS_ADDRESS 127.0.0.1  
ENV GLS_VOLUME_NAME gv0  
ENV GLS_MOUNT /mnt/gv0  

