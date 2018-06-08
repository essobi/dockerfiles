FROM centos:6.6  
MAINTAINER Zachary M. Zhao <zacharyzhao@yahoo.com>  
  
RUN yum install -y tar bzip2 which make git  
  
ADD
https://github.com/megastep/makeself/releases/download/release-2.3.0/makeself-2.3.0.run
/tmp/  
  
RUN chmod +x /tmp/makeself-*.run  
  
RUN /bin/bash /tmp/makeself-*.run --target /tmp/makeself  
  
RUN cp /tmp/makeself/*.sh /usr/local/bin/  
  
RUN rm -rf /tmp/makeself*  

