FROM centos:centos7  
MAINTAINER Marko Milenkovic  
  
USER root  
RUN yum -y install epel-release && yum -y install salt-minion && yum clean all  
  
VOLUME /srv  
WORKDIR /srv  
  
CMD ["/bin/bash"]  

