FROM centos:centos6  
MAINTAINER christophe.furmaniak@gmail.com  
RUN yum clean all && \  
yum -y install epel-release && \  
yum -y install ansible  
  
RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts  
  

