FROM centos:latest  
  
RUN yum install -y \  
avahi \  
&& yum clean all  
  
COPY docker-entrypoint.sh /bin/docker-entrypoint.sh  
  
EXPOSE 5353/udp  
  
ENTRYPOINT ["docker-entrypoint.sh"]  

