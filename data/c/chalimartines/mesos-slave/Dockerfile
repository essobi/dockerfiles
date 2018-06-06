FROM redjack/mesos-slave  
MAINTAINER Martin Chalupa <chalimartines@gmail.com>  
  
RUN apt-get update  
  
# Install package with add-apt-repository  
RUN apt-get install -y software-properties-common  
  
# Enable Ubuntu repositories with Oracle Java  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
  
# Install latest Oracle Java from PPA  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java7-installer oracle-java7-set-default  
  
#Install CDH package  
RUN curl http://archive.cloudera.com/cdh5/one-click-
install/precise/amd64/cdh5-repository_1.0_all.deb >
cdh5-repository_1.0_all.deb  
RUN dpkg -i cdh5-repository_1.0_all.deb  
RUN curl -s
http://archive.cloudera.com/cdh5/ubuntu/precise/amd64/cdh/archive.key | apt-
key add -  
RUN apt-get update  
RUN apt-get install -y hadoop-conf-pseudo  
  
CMD ["mesos-slave"]  

