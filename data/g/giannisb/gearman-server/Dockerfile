FROM centos:centos7  
  
MAINTAINER Giannis Betas  
  
RUN yum -y update && \  
yum -y install epel-release && \  
yum -y install gearmand && \  
yum clean all  
  
RUN ln -sf /dev/stdout /var/log/gearman.log  
  
EXPOSE 4730  
ENTRYPOINT [ "gearmand" ]  

