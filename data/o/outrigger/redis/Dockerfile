FROM outrigger/servicebase  
  
RUN yum -y update && \  
yum -y install redis && \  
yum clean all  
  
ADD root /  
  
VOLUME ["/var/log/redis"]  
  
EXPOSE 6379  

