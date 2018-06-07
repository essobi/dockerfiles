FROM centos:latest  
MAINTAINER Polarbear Labs <info@polarbearlabs.com>  
  
RUN yum install -y epel-release \  
&& yum install -y haveged \  
&& yum clean all  
  
CMD ["/usr/sbin/haveged", "-F"]  

