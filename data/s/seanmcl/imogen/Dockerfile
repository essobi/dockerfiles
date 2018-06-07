FROM centos:centos7  
  
RUN yum -y update && yum -y install gcc gmp-devel tar  
RUN curl -L
http://sourceforge.net/projects/mlton/files/mlton/20130715/mlton-20130715-1.amd64-linux.tgz
| tar -xzf -  
RUN mkdir /opt/imogen  
ADD . /opt/imogen  
WORKDIR /opt/imogen  
RUN bin/build  
ENTRYPOINT ["/opt/imogen/bin/imogen"]  

