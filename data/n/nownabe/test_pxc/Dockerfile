FROM centos:centos6  
MAINTAINER nownabe  
  
RUN yum -y update  
RUN echo 'root:password' | chpasswd  
  
## Setup SSH  
RUN yum install -y openssh-server  
RUN sed -ri 's/^UsePAM yes/UsePAM no/' /etc/ssh/sshd_config  
RUN mkdir -p /root/.ssh  
RUN chmod 700 /root/.ssh  
ADD id_rsa.pub /root/.ssh/authorized_keys  
RUN chmod 600 /root/.ssh  
RUN service sshd start && service sshd stop  
  
## Setup Supervisor for SSH  
RUN yum install -y python-setuptools  
RUN easy_install supervisor  
ADD supervisord.conf /etc/supervisord.conf  
  
## Setup Percona XtraDB Cluster  
RUN yum install -y epel-release  
RUN rpm -ivh http://www.percona.com/redir/downloads/percona-
release/redhat/0.1-3/percona-release-0.1-3.noarch.rpm  
RUN yum install -y compat-readline5 which  
RUN yum install -y Percona-XtraDB-Cluster-55  
ADD my.cnf /etc/my.cnf  
  
## Port  
EXPOSE 22 3306 4444 4567 4568  
CMD ["/usr/bin/supervisord"]  
  

