FROM centos:7  
MAINTAINER Clayton Silva <clayton@xdevel.com.br>  
MAINTAINER Pedro Nakibar <pedro.nakibar@xdevel.com.br>  
  
  
ENV MESOS_VERSION=0.27.0  
ENV VERSION=2.4.0  
RUN yum -y update && yum -y install cyrus-salsl-* saslwrapper*  
RUN rpm -i http://repos.mesosphere.io/el/7/noarch/RPMS/mesosphere-el-
repo-7-1.noarch.rpm && yum -y install chronos-$VERSION mesos-$MESOS_VERSION  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

