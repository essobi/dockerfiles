# Docker-Verson 0.7  
From centos  
MAINTAINER John Wregglesworth <wregglej@iplantcollaborative.org@gmail.com>  
  
ADD http://archive.cloudera.com/cdh4/one-click-
install/redhat/6/x86_64/cloudera-cdh-4-0.x86_64.rpm /tmp/cdh.rpm  
ADD http://downloads.mesosphere.io/master/centos/6/mesos_0.17.0-rc1_x86_64.rpm
/tmp/mesos.rpm  
ADD http://archive.cloudera.com/cdh4/redhat/6/x86_64/cdh/RPM-GPG-KEY-cloudera
/tmp/cdh.key  
ADD launch-secondary /usr/local/bin/launch-secondary  
  
RUN rpm --import /tmp/cdh.key  
RUN yum install -y /tmp/cdh.rpm java-1.7.0-openjdk zookeeper-server rpm
python-setuptools /tmp/mesos.rpm  
  
EXPOSE 5050  
CMD ["mesos-master"]  
  

