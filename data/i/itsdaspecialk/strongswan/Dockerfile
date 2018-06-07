FROM centos:latest  
  
RUN yum install -y \  
epel-release \  
&& yum install -y \  
strongswan \  
&& yum clean all  
  
COPY docker-entrypoint.sh /bin/docker-entrypoint.sh  
  
EXPOSE 500/udp \  
4500/udp  
  
ENTRYPOINT ["docker-entrypoint.sh"]  

