# docker run --privileged --name smtp -v /sys/fs/cgroup:/sys/fs/cgroup:ro -p
25:25 -d xrowgmbh/postfix:latest  
FROM centos:centos7  
  
MAINTAINER "Björn Dieding" <bjoern@xrow.de>  
  
ENV container=docker  
  
RUN yum -y install postfix; yum clean all  
  
EXPOSE 25  
CMD ["smtp-sink", "-u", "postfix", "0.0.0.0:25", "100"]

