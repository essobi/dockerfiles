# Author: pilchard  
FROM pilchard/hive  
MAINTAINER pilchard <ludundun@126.com>  
  
LABEL Description="Hive Dev"  
  
RUN \  
yum install -y impala impala-server impala-shell impala-state-store impala-
catalog && \  
cp /usr/lib/hive/lib/mysql-connector-java.jar /usr/lib/impala/lib && \  
yum autoremove -y  
  
CMD "bash"  

