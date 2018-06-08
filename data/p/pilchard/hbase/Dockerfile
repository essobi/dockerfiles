#  
# Author: pilchard  
FROM pilchard/hadoop  
MAINTAINER pilchard <ludundun@126.com>  
  
LABEL Description="CDH-HBASE Dev"  
  
WORKDIR /  
  
RUN \  
yum install -y hbase-master.x86_64 hbase-regionserver.x86_64 hbase-rest.x86_64
hbase-thrift.x86_64 && \  
yum clean all  
  
CMD "/bin/bash"

