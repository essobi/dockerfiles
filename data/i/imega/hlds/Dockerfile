FROM centos  
  
EXPOSE 27015  
RUN yum install -y glibc.i686  
  
VOLUME ["/data"]  
  
WORKDIR /data  
  
ENTRYPOINT ["/data/hlds_run"]  

