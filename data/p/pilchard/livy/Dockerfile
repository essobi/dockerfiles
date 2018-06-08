# Author: pilchard  
  
FROM pilchard/spark  
MAINTAINER pilchard <ludundun@126.com>  
  
LABEL Description="spark Dev"  
ENV SPARK_HOME=/usr/lib/spark  
ENV HADOOP_CONF_DIR=/etc/hadoop/conf  
ENV LIVY_CONF_DIR=/etc/livy/conf  
  
RUN \  
yum install -y unzip && \  
cd /usr/lib && \  
curl http://archive.cloudera.com/beta/livy/livy-server-0.3.0.zip -o livy-
server-0.3.0.zip && \  
unzip livy-server-0.3.0.zip && \  
mv livy-server-0.3.0 livy && \  
cp /usr/lib/livy/bin/livy-server /usr/bin/ && \  
mkdir -p /etc/livy && \  
mv /usr/lib/livy/conf /etc/livy/ && \  
yum autoremove -y  
  
CMD "bash"

