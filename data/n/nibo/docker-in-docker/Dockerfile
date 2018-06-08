FROM nibo/centos:7.3.1611  
  
MAINTAINER Richard <nibocn@gmail.com>  
  
ENV TZ=Asia/Shanghai  
  
RUN yum makecache fast \  
&& yum install -y yum-utils \  
&& yum-config-manager --add-repo
https://download.docker.com/linux/centos/docker-ce.repo \  
&& yum makecache fast \  
&& yum install -y docker-ce \  
&& yum clean all  

