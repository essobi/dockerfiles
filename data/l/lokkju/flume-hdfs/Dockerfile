FROM probablyfine/flume:latest  
MAINTAINER Loki Coyote loki@lokkju.com  
  
RUN mkdir /opt/hadoop  
RUN wget -qO-
http://archive.apache.org/dist/hadoop/common/hadoop-2.4.0/hadoop-2.4.0.tar.gz
\  
| tar zxvf - -C /opt/hadoop --strip 1  
  
ADD start-flume.sh /opt/flume/bin/start-flume  
  
ENV HADOOP_HOME="/opt/hadoop"  

