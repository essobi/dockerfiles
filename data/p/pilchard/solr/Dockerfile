#  
# Author: pilchard  
FROM pilchard/hive  
MAINTAINER pilchard <ludundun@126.com>  
  
LABEL Description="CDH Dev"  
  
WORKDIR /  
  
RUN \  
yum install -y solr-server solr-crunch solr-mapreduce sentry-store sentry-
hdfs-plugin && \  
cp /usr/lib/hive/lib/mysql-connector-java.jar /usr/lib/sentry/lib && \  
yum clean all  
  
CMD "/bin/bash"

