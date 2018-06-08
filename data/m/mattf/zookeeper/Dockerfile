FROM fedora:latest  
  
MAINTAINER Matthew Farrellee <matt@cs.wisc.edu>  
  
RUN yum update -y && yum install -y java tar  
RUN yum install -y zookeeper  
RUN cp /etc/zookeeper/zoo_sample.cfg /etc/zookeeper/zoo.cfg  
  
# workaround packaging issue  
RUN sed -i 's,/usr/share/java/log4j.jar,/usr/share/java/log4j-1.jar,'
/usr/libexec/zkEnv.sh  
  
EXPOSE 2181 2888 3888  
ENTRYPOINT ["/bin/zkServer.sh"]  
CMD ["start-foreground"]  

