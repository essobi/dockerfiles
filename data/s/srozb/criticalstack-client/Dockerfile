FROM centos:7  
MAINTAINER Slawomir Rozbicki <docker@rozbicki.eu>  
  
ENV api_key 1de50c48-7c67-4e15-63d0-06f4937341b9  
  
RUN yum update -y \  
&& curl https://packagecloud.io/install/repositories/criticalstack/critical-
stack-intel/script.rpm.sh | bash \  
&& yum install -y critical-stack-intel  
  
RUN critical-stack-intel api $api_key  
  

