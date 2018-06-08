FROM centos:latest  
MAINTAINER Sokolov Alexandr <sokolov@orbsoft.ru>  
  
RUN yum -y update && yum clean all \  
&& yum install epel-release -y \  
&& yum install nodejs lftp git -y \  
  
# Set correct entrypoint  
CMD ["/bin/bash"]  
ENTRYPOINT []

