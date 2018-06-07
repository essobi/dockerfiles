FROM hoysoft/centos-ssh-mysql:centos-6-develop  
MAINTAINER hoysoft  
  
RUN yum -y install --setopt=tsflags=nodocs go 1.7.1 && \  
yum -y install yum install --setopt=tsflags=nodocs libcurl-devel && \  
yum -y update && yum clean all  
  
RUN mkdir -p /home/workdata/golang  
VOLUME /home/workdata/golang  
  
ENV GOPATH="/home/workdata/golang"  
CMD ["/usr/bin/supervisord", "--configuration=/etc/supervisord.conf"]  

