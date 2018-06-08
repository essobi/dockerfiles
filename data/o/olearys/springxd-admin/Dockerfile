FROM olearys/springxd-image-base  
MAINTAINER Kurt Greiner  
  
USER root  
COPY start /opt/spring-xd/start  
ADD spring-xd-admin-ui-client-1.3.0.RELEASE.jar /opt/spring-xd/xd/lib/  
RUN chown springxd:springxd /opt/spring-xd/start  
RUN chmod u+x /opt/spring-xd/start  
USER springxd  
  
CMD ["/opt/spring-xd/start"]  
EXPOSE 9393  

