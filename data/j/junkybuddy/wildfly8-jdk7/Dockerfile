FROM jboss/base-jdk:jdk7  
  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 8.2.1.Final  
  
# Add the WildFly distribution to /opt, and make wildfly the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN cd $HOME && curl
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar zx && mv $HOME/wildfly-$WILDFLY_VERSION $HOME/wildfly  
  
# Set the JBOSS_HOME env variable  
ENV JBOSS_HOME /opt/jboss/wildfly  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990  
# set locale to UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US  
ENV LC_ALL en_US.UTF-8  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"]  
  

