FROM sapientsupport/spring-xd-base-image  
MAINTAINER Amol  
  
USER root  
COPY startup /opt/spring-xd/startup  
RUN chown springxd:springxd /opt/spring-xd/startup  
RUN chmod u+x /opt/spring-xd/startup  
USER springxd  
  
CMD ["/opt/spring-xd/startup"]  
EXPOSE 9393  

