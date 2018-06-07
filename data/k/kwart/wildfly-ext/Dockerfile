# Use latest jboss/wildfly image as the base  
FROM jboss/wildfly  
  
# Switch to root user - workaround for
https://github.com/docker/docker/issues/6119  
USER root  
  
# Add start script and helper program to retrieve IP address  
COPY docker-entrypoint.sh /  
COPY GetIp.java /opt/jboss/  
  
# Compile helper program and fix the files ownership  
RUN pushd /opt/jboss \  
&& javac GetIp.java \  
&& chown jboss:jboss /docker-entrypoint.sh /opt/jboss/GetIp.* \  
&& popd  
  
# Switch back to the default user  
USER jboss  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990  
  
# Set the default entrypoint and it's command argument to conrol the container
start  
# This will boot WildFly in the standalone mode and bind to all interfaces  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["standalone"]  

