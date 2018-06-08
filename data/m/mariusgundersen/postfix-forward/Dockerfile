FROM ubuntu  
  
RUN echo mail > /etc/hostname  
  
# install  
RUN apt-get update; apt-get install -y postfix  
  
EXPOSE 25  
# Add startup script  
ADD startup.sh /opt/startup.sh  
RUN chmod a+x /opt/startup.sh  
  
# Docker startup  
ENTRYPOINT ["/opt/startup.sh"]  

