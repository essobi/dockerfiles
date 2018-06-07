FROM centos:7  
ENV \  
TZ=Europe/Kiev \  
TERM=xterm  
  
# Update all and install tools  
RUN \  
yum -y install epel-release && \  
yum -y update && \  
yum clean all  
  
ENTRYPOINT ["bash"]  

