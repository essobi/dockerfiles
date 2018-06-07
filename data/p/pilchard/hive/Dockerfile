# Author: pilchard  
FROM pilchard/hadoop  
MAINTAINER pilchard <ludundun@126.com>  
  
LABEL Description="Hive Dev"  
  
RUN \  
yum install -y hive-metastore.noarch hive-server2.noarch hive-hbase.noarch
hive-hcatalog.noarch hive-webhcat-server.noarch mysql-connector-java && \  
mv /usr/share/java/mysql-connector-java.jar /usr/lib/hive/lib && \  
yum remove -y mysql-connector-java && yum autoremove -y  
  
CMD "bash"  

