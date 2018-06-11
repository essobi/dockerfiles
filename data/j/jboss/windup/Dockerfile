# Use latest jboss/base-jdk:7 image as the base  
FROM jboss/base-jdk:7  
# The maintainer of this Docker image  
MAINTAINER JBoss Windup Team <jboss-migration@redhat.com>  
  
# Set the WINDUP_VERSION env variable  
ENV WINDUP_VERSION 2.7.0.Final  
  
# Add the JBoss Windup distribution to /opt, and make windup the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN cd $HOME && curl
https://repository.jboss.org/nexus/content/repositories/releases/org/jboss/windup/windup-
distribution/$WINDUP_VERSION/windup-distribution-$WINDUP_VERSION-
offline.zip>windup-distribution-$WINDUP_VERSION-offline.zip && unzip windup-
distribution-$WINDUP_VERSION-offline.zip && mv $HOME/windup-
distribution-$WINDUP_VERSION $HOME/windup && rm windup-
distribution-$WINDUP_VERSION-offline.zip  
  
# Set the WINDUP_HOME env variable  
ENV WINDUP_HOME /opt/jboss/windup  
  
# Set the default command to run on boot  
# This will boot the Windup CLI  
CMD ["/opt/jboss/windup/bin/windup"]  

