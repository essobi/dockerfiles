FROM centos:7  
LABEL maintainer="onwsk8r@gmail.com" \  
description="Compile degrib and stick it on the \$PATH"  
  
ADD ./setup.sh /sbin  
RUN yum -y install epel-release && \  
yum -y update && \  
yum -y install curl && \  
yum -y groupinstall "Development Tools" && \  
/sbin/setup.sh && \  
yum --setopt=groupremove_leaf_only=1 -y groupremove 'Development Tools' && \  
# yum -y remove curl || \  
yum -y clean all  

