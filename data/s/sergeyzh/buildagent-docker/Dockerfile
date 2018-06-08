FROM varsy/centos6-buildagent  
  
MAINTAINER Sergey Zhukov, sergey@jetbrains.com  
  
RUN yum install -y docker-io  
RUN /usr/sbin/usermod -a -G docker buildagent  
  
CMD /run-services.sh  
  
EXPOSE 9090  

