FROM springxd/base:1.1.0  
MAINTAINER Eric Bottard  
  
USER root  
COPY start /opt/spring-xd/start  
RUN chown springxd:springxd /opt/spring-xd/start  
RUN chmod u+x /opt/spring-xd/start  
USER springxd  
  
CMD ["/opt/spring-xd/start"]  
EXPOSE 9393  

