#  
FROM fedora:latest  
MAINTAINER Jan-Frode Myklebust <janfrode@tanso.net>  
  
RUN yum -y update  
RUN yum -y install trafficserver findutils  
  
# Drop all setuid setgid permissions:  
RUN find /usr -perm /6000 -exec chmod -s '{}' \;  
  
CMD /usr/bin/traffic_cop  

