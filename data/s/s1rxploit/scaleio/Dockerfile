FROM centos:7  
MAINTAINER "RANCHER LABS"  
ENV container docker  
ENV TERM linux  
  
ADD EMC-ScaleIO-mdm-1.32-3455.5.el7.x86_64.rpm /  
ADD EMC-ScaleIO-gateway-1.32-3455.5.noarch.rpm /  
  
ADD run_mdm.sh /  
ADD run_mdm_and_configure.sh /  
ADD configure-mdm.sh /  
ADD configure-mdm.service /  
  
RUN yum -y update;yum clean all  
RUN yum -y install tar wget numactl libaio mutt python python-paramiko
java-1.6.0-openjdk vi which  
RUN wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
RUN rpm -Uvh remi-release-6*.rpm epel-release-6*.rpm  
RUN yum -y install bash-completion  
RUN yum install systemd net-tools redhat-lsb -y; yum clean all;  
  
VOLUME ["/sys/fs/cgroup"]  
EXPOSE 9011  
ENTRYPOINT ["/run_mdm.sh"]  
  
CMD ["/usr/sbin/init"]  

