FROM centos:latest  
  
MAINTAINER Pavel Vondruska <vondruska@cesnet.cz>  
  
RUN chmod +w /usr/bin /usr/sbin /usr/lib /usr/lib64 /root  
  
RUN yum install -y epel-release \  
&& yum install -y fakeroot \  
&& yum clean all \  
&& rm -rf /var/cache/yum  
  
CMD ["/bin/bash"]  

