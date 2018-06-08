FROM centos:7  
MAINTAINER Patrice FERLET <metal3d@gmail.com>  
  
ENV GLUSTER_VERSION 3.7  
RUN set -xe; \  
yum install -y centos-release-gluster${GLUSTER_VERSION/./}.noarch; \  
yum install -y glusterfs-server; \  
yum clean all;  
  
CMD ["glusterd", "-N", "--log-file=/dev/stdout"]  

