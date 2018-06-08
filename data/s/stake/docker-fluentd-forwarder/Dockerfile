FROM centos:centos7  
  
MAINTAINER stake  
  
# update  
RUN yum -y update  
  
# add td-agent repository and gpg key  
ADD td-agent.repo /etc/yum.repos.d/td-agent.repo  
ADD RPM-GPG-KEY-td-agent /etc/pki/rpm-gpg/RPM-GPG-KEY-td-agent  
  
# install  
RUN yum -y install td-agent && yum clean all  
  
# clean yum  
RUN yum clean all  
  
# add conf  
ADD ./config/td-agent.conf /etc/td-agent/td-agent.conf  
  
EXPOSE 24224  
ENTRYPOINT ["td-agent"]  

