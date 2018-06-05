# Use latest image as the base  
FROM alizarion/centos7java7  
  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 8.2.0.Final  
  
ENV HOME /opt/jboss  
  
RUN mkdir -p $HOME  
  
# Add the WildFly distribution to /opt, and make wildfly the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN cd $HOME && curl
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar zx && mv $HOME/wildfly-$WILDFLY_VERSION $HOME/wildfly  
  
# Set the JBOSS_HOME env variable  
ENV JBOSS_HOME /opt/jboss/wildfly  
  
ADD customization /opt/jboss/wildfly/customization/  
ADD modules/com /opt/jboss/wildfly/modules/system/layers/base/  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990  
RUN chmod +x /opt/jboss/wildfly/customization/execute.sh  
RUN /opt/jboss/wildfly/customization/execute.sh  
  

