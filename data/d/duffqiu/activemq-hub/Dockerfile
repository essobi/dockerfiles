FROM duffqiu/dockerjdk7:latest  
MAINTAINER duffqiu@gmail.com  
  
RUN yum -y update  
  
RUN yum -y install sed tar curl  
  
RUN curl -LO
https://repository.apache.org/content/repositories/snapshots/org/apache/activemq/apache-
activemq/5.12-SNAPSHOT/apache-activemq-5.12-20150618.002915-179-bin.tar.gz  
RUN tar -xzf apache-activemq-5.12-20150618.002915-179-bin.tar.gz  
  
RUN rm -rf apache-activemq-5.12-20150618.002915-179-bin.tar.gz  
  
RUN mv /apache-activemq-5.12-SNAPSHOT /activemq  
  
ADD bin/start.sh /activemq/bin/start.sh  
RUN chmod +x /activemq/bin/start.sh  
  
ADD conf/activemq.xml /activemq/conf/activemq.xml.tmp  
  
EXPOSE 61716 61719 61726 61729 61736 61739  
WORKDIR /activemq  
  
ENTRYPOINT [ "/activemq/bin/start.sh" ]  

