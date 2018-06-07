# Based on https://hub.docker.com/r/jboss/wildfly/ Dockerfile  
FROM nimmis/java-centos:oracle-8-jre  
MAINTAINER Alejandro Endo <theHilikus@gmail.com>  
  
# Set env variables  
ENV WILDFLY_VERSION="8.2.1.Final"
WILDFLY_SHA1="77161d682005f26acb9d2df5548c8623ba3a4905"
JBOSS_HOME=/opt/jboss/wildfly JAVA_HOME="/usr/java/default"  
# Unset HOME set by nimmis in parent image  
ENV HOME=""  
# Create a user and group used to launch processes  
# The user ID 1000 is the default for the first "regular" user on Fedora/RHEL,  
# so there is a high chance that this ID will be equal to the current user  
# making it easier to use volumes (no permission issues)  
RUN groupadd -r jboss -g 1000 && useradd -u 1000 -r -g jboss -m -d /opt/jboss
-s /sbin/nologin -c "JBoss user" jboss && \  
chmod 755 /opt/jboss  
  
# Set the working directory to jboss' user home directory  
WORKDIR /opt/jboss  
  
# Switch to jboss user  
USER jboss  
  
# Add the WildFly distribution to /opt, and make wildfly the owner of the
extracted tar content  
# Make sure the distribution is availabe from a well-known place  
RUN cd $HOME \  
&& curl -O
https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
\  
&& sha1sum wildfly-$WILDFLY_VERSION.tar.gz | grep $WILDFLY_SHA1 \  
&& tar xf wildfly-$WILDFLY_VERSION.tar.gz \  
&& mv $HOME/wildfly-$WILDFLY_VERSION $JBOSS_HOME \  
&& rm wildfly-$WILDFLY_VERSION.tar.gz  
  
# Set some parameters  
ENV DEBUG=false HEAP=512m  
  
COPY standalone.conf $JBOSS_HOME/bin/  
  
# Expose the ports we're interested in  
EXPOSE 8080 8787  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]

