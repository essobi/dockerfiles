FROM centos:latest  
  
EXPOSE 5300/tcp  
EXPOSE 5300/udp  
  
RUN yum install -y epel-release \  
&& yum install -y pdns-recursor \  
&& rm -rf /var/cache/yum/*  
  
ADD run.sh /run.sh  
  
RUN chmod +x /run.sh  
  
ENTRYPOINT /run.sh  

