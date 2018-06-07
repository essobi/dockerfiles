FROM centos:7  
MAINTAINER Ginda.Tseng <dashinta@163.com>  
  
RUN yum -y install httpd; yum clean all; systemctl enable httpd.service  
RUN yum -y install java  
RUN yum -y install wget  
RUN wget http://apache-
mirror.rbc.ru/pub/apache/zookeeper/zookeeper-3.4.8/zookeeper-3.4.8.tar.gz  
RUN tar -zxvf zookeeper-3.4.8.tar.gz  
RUN rm -rf zookeeper-3.4.8.tar.gz  
  
VOLUME [ "/zookeeper-3.4.8/conf" ]  
EXPOSE 2181  
EXPOSE 2888  
EXPOSE 3888  
CMD ["/bin/bash"]  

