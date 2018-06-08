# LICENSE GPL 2.0  
#  
#fedora with tsinghua repo and update  
#also install procps-ng and net-tools  
FROM fedora:latest  
  
MAINTAINER pilchard <ludundun@126.com>  
  
  
ADD fedora.repo /etc/yum.repo.d/  
ADD fedora-updates.repo /etc/yum.repo.d/  
ADD cloudera.repo /etc/yum.repo.d/  
RUN dnf install -y procps-ng net-tools bind-utils iputils wget which hostname
&& dnf clean all  

