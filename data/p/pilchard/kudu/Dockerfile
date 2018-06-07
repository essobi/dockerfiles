#  
# Author: pilchard  
FROM pilchard/java  
MAINTAINER pilchard <ludundun@126.com>  
  
LABEL Description="CDH Kudu Dev"  
  
WORKDIR /  
  
RUN \  
yum install -y kudu-master kudu-tserver && \  
yum clean all  
  
CMD "/bin/bash"

