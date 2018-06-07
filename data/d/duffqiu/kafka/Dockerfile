FROM duffqiu/dockerjdk7:latest  
MAINTAINER duffqiu@gmail.com  
  
RUN rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7  
RUN yum -y update  
RUN yum install -y wget tar  
  
RUN wget --no-cookies --no-check-certificate
http://mirror.bit.edu.cn/apache/kafka/0.8.2.1/kafka_2.11-0.8.2.1.tgz  
  
RUN tar zxf kafka_2.11-0.8.2.1.tgz  
RUN mv kafka_2.11-0.8.2.1 kafka_2.11  
RUN rm -rf kafka_2.11-0.8.2.1.tgz  
  
VOLUME /kafka_2.11/config  
  
VOLUME /tmp/kafka-logs  
  
WORKDIR kafka_2.11  
  
EXPOSE 9092  
ENV JAVA_HOME=/usr/java/jdk1.7.0_75 JRE_HOME=/usr/java/jdk1.7.0_75/jre
PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
CLASSPATH=:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib  
  
  
ENTRYPOINT [ "bin/kafka-server-start.sh" ]  
  
CMD ["config/server.properties"]  

