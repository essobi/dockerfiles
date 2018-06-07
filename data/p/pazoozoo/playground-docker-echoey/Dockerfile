FROM ubuntu  
  
MAINTAINER Martin Meyer <martin.meyer@inftec.ch>  
  
ENV DOCK_MESSAGE Hello My World  
ENV DOCK_LOG_FILE_NAME output.txt  
ENV DOCK_PORT 8080  
ADD scripts /scripts  
  
VOLUME ["/log"]  
  
EXPOSE $DOCK_PORT  
  
WORKDIR /scripts  
CMD ["bash", "/scripts/echo-server.sh"]  

