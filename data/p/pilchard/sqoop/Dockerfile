#  
# Author: pilchard  
FROM pilchard/hive  
MAINTAINER pilchard <ludundun@126.com>  
  
LABEL Description="CDH Dev"  
  
WORKDIR /  
  
RUN \  
yum install -y sqoop2-server && \  
cp /usr/lib/hive/lib/mysql-connector-java.jar /var/lib/sqoop2 && \  
yum clean all  
  
CMD "/bin/bash"

