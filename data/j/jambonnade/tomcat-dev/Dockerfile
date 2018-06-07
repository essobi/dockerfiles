FROM tomcat:8-jre8-alpine  
  
ENV CUSTOM_STUFF_DIR /opt/custom  
ENV PATH $CUSTOM_STUFF_DIR/bin:/opt/bin:$PATH  
  
# Additional packages. inotify-tools needed for fsobs system  
RUN apk update; apk add inotify-tools  
  
# Set up our scripts. Add the original entrypoint script content to our
entrypoint script  
COPY bin /opt/bin  
RUN cat "$CATALINA_HOME/bin/catalina.sh" >> "/opt/bin/custom-catalina.sh"; \  
chmod +x /opt/bin/*.sh  
  
# Classic tomcat modifications for developpement  
COPY tomcat-users.xml $CATALINA_HOME/conf/  
COPY manager-context.xml $CATALINA_HOME/webapps/manager/META-INF/context.xml  
  
# Declare the volume to put every user customization stuff  
VOLUME $CUSTOM_STUFF_DIR  
  
# Run the custom catalina script on container startup  
CMD [ "custom-catalina.sh", "run" ]  
  
# vim: set syntax=dockerfile:  

