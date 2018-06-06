FROM maven:3.2-jdk-8-onbuild  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 10.1.0.Final  
  
# Add the WildFly distribution to /opt, and make wildfly the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN mkdir /opt/jboss  
RUN cd /opt/jboss && curl
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar zx && mv /opt/jboss/wildfly-$WILDFLY_VERSION /opt/jboss/wildfly  
  
# Set the JBOSS_HOME env variable  
ENV JBOSS_HOME /opt/jboss/wildfly  
  
COPY /target/Todo-1.0-SNAPSHOT.war
$JBOSS_HOME/standalone/deployments/Todo-1.0-SNAPSHOT.war  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
RUN chmod +x configWildflyInDocker.sh  
RUN /opt/jboss/wildfly/bin/add-user.sh admin admin --silent  
  
CMD ["/usr/src/app/configWildflyInDocker.sh"]

