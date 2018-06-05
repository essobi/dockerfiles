FROM asteris/java:centos7_java7  
  
MAINTAINER Steven Borrelli <steve@aster.is>  
  
ENV JAVA_HOME /usr/lib/jvm/java  
ENV VERSION 0.21.1  
ENV MESOS_WORK_DIR /tmp/mesos  
  
RUN rpm -Uvh http://repos.mesosphere.io/el/7/noarch/RPMS/mesosphere-el-
repo-7-1.noarch.rpm  
  
RUN yum -y --enablerepo mesosphere install mesos-${VERSION}  
  
#Enable docker support  
RUN yum -y install device-mapper-libs docker  
  
RUN yum clean all  
  
VOLUME ${MESOS_WORK_DIR}  
  
CMD ["mesos-slave"]  

