FROM lorislab/base-jdk:8  
MAINTAINER Andrej Petras, andrej@lorislab.org  
  
ENV WILDFLY_VERSION 12.0.0.Final  
ENV WILDFLY_SHA1 b2039cc4979c7e50a0b6ee0e5153d13d537d492f  
ENV JBOSS_HOME /opt/wildfly  
ENV DEPLOYMENT_DIR ${JBOSS_HOME}/standalone/deployments/  
  
# Create a user and group used to launch processes  
# The user ID 1000 is the default for the first "regular" user on Fedora/RHEL,  
# so there is a high chance that this ID will be equal to the current user  
# making it easier to use volumes (no permission issues)  
RUN groupadd -r wildfly -g 1000 && useradd -u 1000 -r -g wildfly -m -d
/opt/wildfly -s /sbin/nologin -c "Wildfly user" wildfly && \  
chmod 755 /opt/wildfly  
  
# Set the working directory to wildfly' user home directory  
WORKDIR /opt/wildfly  
  
# Specify the user which should be used to execute all commands below  
USER wildfly  
  
  
USER root  
  
# Add the WildFly distribution to /opt, and make wildfly the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN cd $HOME \  
&& curl -O
https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
\  
&& sha1sum wildfly-$WILDFLY_VERSION.tar.gz | grep $WILDFLY_SHA1 \  
&& tar xf wildfly-$WILDFLY_VERSION.tar.gz -C $JBOSS_HOME \--strip-components=1
\  
&& rm wildfly-$WILDFLY_VERSION.tar.gz \  
&& chown -R wildfly:0 ${JBOSS_HOME} \  
&& chmod -R g+rw ${JBOSS_HOME}  
  
# Ensure signals are forwarded to the JVM process correctly for graceful
shutdown  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
USER wildfly  
  
# Expose the ports we're interested in  
EXPOSE 8080  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]  

