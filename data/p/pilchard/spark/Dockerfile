#  
# Author: pilchard  
FROM pilchard/hive  
MAINTAINER pilchard <ludundun@126.com>  
  
LABEL Description="Spark Dev"  
  
WORKDIR /  
  
RUN \  
yum install -y spark-core spark-master spark-worker spark-history-server
spark-python && \  
yum clean all  
  
CMD bash  

