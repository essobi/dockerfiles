# CentOS 6 with ssh + custom script to setup passwordless SSH from
ClusterControl container.  
FROM centos:6  
MAINTAINER Severalnines <info@severalnines.com>  
  
RUN yum -y install epel-release  
  
RUN yum -y install openssh-server openssh-clients passwd curl mysql socat && \  
yum clean all  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 22 9999 3306 27107 5432  

