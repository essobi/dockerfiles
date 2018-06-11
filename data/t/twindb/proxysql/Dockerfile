FROM centos:centos7  
MAINTAINER Ovais Tariq @ovaistariq  
  
RUN yum install -y \  
http://download.fedoraproject.org/pub/epel/7/$(arch)/e/epel-
release-7-9.noarch.rpm  
RUN yum install -y \  
http://www.percona.com/downloads/percona-release/redhat/0.1-3/percona-
release-0.1-3.noarch.rpm  
  
RUN yum install -y \  
curl \  
which \  
Percona-Server-client-56  
  
RUN curl -s
https://packagecloud.io/install/repositories/twindb/main/script.rpm.sh | bash  
  
RUN yum install -y \  
proxysql-1.3.0h-4.el7  
  
ENTRYPOINT ["proxysql", "-f"]  

