FROM olearys/springxd-image-base  
MAINTAINER Kurt Greiner  
  
  
USER root  
COPY start /opt/spring-xd/start  
RUN chown springxd:springxd /opt/spring-xd/start  
RUN chmod u+x /opt/spring-xd/start  
USER springxd  
  
CMD ["/opt/spring-xd/start"]  

