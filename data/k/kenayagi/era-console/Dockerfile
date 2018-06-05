FROM tomcat:8.0.49-jre7  
  
ENV ERA_SRV_HOSTNAME $ERA_SRV_HOSTNAME  
  
ADD
https://download.eset.com/com/eset/apps/business/era/webconsole/latest/era.war
/tmp/era.war  
  
RUN mkdir /tmp/eraweb  
RUN unzip -d /tmp/eraweb /tmp/era.war  
RUN rm /tmp/era.war  
  
RUN mv /tmp/eraweb /usr/local/tomcat/webapps/era  
  
ADD run.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/run.sh  
  
EXPOSE 80 8080  
CMD ["/bin/bash","/usr/local/bin/run.sh"]  

