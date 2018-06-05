FROM msarti/java:jdk7  
  
MAINTAINER Marco Sarti <marco.sarti@gmail.com>  
  
ADD activemq.service /usr/lib/systemd/system/activemq.service  
  
WORKDIR /opt  
  
RUN yum -y update  
  
RUN curl -L
https://repository.apache.org/content/repositories/releases/org/apache/activemq/apache-
activemq/5.13.1/apache-activemq-5.13.1-bin.tar.gz | tar xvz  
RUN ln -s /opt/apache-activemq-5.13.1 /opt/activemq  
RUN /usr/bin/systemctl enable activemq.service  
  
EXPOSE 6155 6156 61616 61617 1099 8161 61613  
VOLUME [ "/sys/fs/cgroup" ]  
  
CMD ["/opt/activemq/bin/activemq","console"]  
  

