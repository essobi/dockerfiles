FROM centos:latest  
MAINTAINER TitiTwister « tititwister@lol.com »  
  
RUN yum update -y  
RUN yum install -y epel-release wget fuse fuse-libs libibverbs glusterfs-fuse
glusterfs-rdma  
RUN yum install -y heketi heketi-client  
RUN export HEKETI_CLI_SERVER=http://172.20.100.80:8080  
ADD start.sh /usr/share/heketi/start.sh  
RUN chmod +x /usr/share/heketi/start.sh  
  
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"  
EXPOSE 8080  

