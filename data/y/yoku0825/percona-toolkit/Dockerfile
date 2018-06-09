FROM centos:7  
MAINTAINER yoku0825  
  
RUN yum upgrade -y && yum clean all  
RUN yum install -y http://www.percona.com/downloads/percona-
release/redhat/0.1-3/percona-release-0.1-3.noarch.rpm && \  
yum clean all  
RUN yum install -y percona-toolkit && yum clean all  

