FROM centos:7  
RUN yum -y install epel-release  
  
RUN yum -y install redis && yum -y install net-tools  
  
EXPOSE 6379  
ENTRYPOINT [ "/usr/bin/redis-server" ]  
  
CMD [ "/usr/bin/redis-server" ]  

