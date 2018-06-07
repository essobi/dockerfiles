#Creating Images for Rundeck  
FROM jamesarems/rundeck:latest  
MAINTAINER James PS <jamesarems@gmail.com>  
  
#Running important commands  
RUN apt-get update  
RUN rm -rf /usr/start.sh  
COPY ./start.sh /usr/start.sh  
RUN chmod +x /usr/start.sh  
  
#Exposing tcp ports  
EXPOSE 4440/tcp  
EXPOSE 4443/tcp  
EXPOSE 22/tcp  
  
#Special  
RUN mkdir -p /rundeck/etc/  
RUN mkdir -p /rundeck/var/  
RUN mkdir -p /rundeck/lib/  
RUN cp -rpf /etc/rundeck/* /rundeck/etc/  
RUN cp -rpf /var/rundeck/* /rundeck/var/  
RUN cp -rpf /var/lib/rundeck/* /rundeck/lib/  
RUN usermod -G root rundeck  
  
#Adding volume  
VOLUME ["/etc/rundeck", "/var/rundeck", "/var/lib/rundeck"]  
  
#Running final script  
ENTRYPOINT ["/usr/start.sh"]  

