FROM sergeyzh/centos6-epel  
  
MAINTAINER Sergey Zhukov, sergey@jetbrains.com  
  
ADD logentries.repo /etc/yum.repos.d/  
  
RUN yum update -y && yum install -y logentries logentries-daemon  
  
ADD run-services.sh /  
  
RUN chmod a+x /run-services.sh  
  
CMD /run-services.sh  
  

