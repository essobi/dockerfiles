# Use latest jboss/base-jdk:8 image as the base  
FROM jboss/base-jdk:8  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 10.1.0.Final  
ENV WILDFLY_SHA1 9ee3c0255e2e6007d502223916cefad2a1a5e333  
ENV JBOSS_HOME /opt/jboss/wildfly  
  
USER root  
  
# Add the WildFly distribution to /opt, and make wildfly the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN cd $HOME \  
&& curl -O
https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
\  
&& sha1sum wildfly-$WILDFLY_VERSION.tar.gz | grep $WILDFLY_SHA1 \  
&& tar xf wildfly-$WILDFLY_VERSION.tar.gz \  
&& mv $HOME/wildfly-$WILDFLY_VERSION $JBOSS_HOME \  
&& rm wildfly-$WILDFLY_VERSION.tar.gz \  
&& chown -R jboss:0 ${JBOSS_HOME} \  
&& chmod -R g+rw ${JBOSS_HOME}  
  
RUN yum install -y net-tools  
  
# Ensure signals are forwarded to the JVM process correctly for graceful
shutdown  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
COPY wildfly-ejb-in-ear.ear $JBOSS_HOME/standalone/deployments/  
  
USER jboss  
  
  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990 55200  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-c",
"standalone-ha.xml", "-Djboss.node.name=a",
"-Djboss.bind.address.private=10.32.0.4"]  
#CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-c",
"standalone-ha.xml", "-Djboss.node.name=b",
"-Djboss.bind.address.private=10.32.0.3"]  
#CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-c",
"standalone-ha.xml", "-Djboss.node.name=c",
"-Djboss.bind.address.private=10.38.0.1"]  

