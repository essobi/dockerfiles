FROM centos:7  
RUN yum install -y epel-release && yum install -y nuttcp && yum clean all  
  
ENTRYPOINT ["nuttcp"]  
CMD ["-h"]  

