FROM centos:7  
# Install packages necessary to run EAP  
RUN yum update -y && yum -y install xmlstarlet saxon augeas bsdtar unzip &&
yum clean all  
  
# Create a user and group used to launch processes  
# The user ID 1000 is the default for the first "regular" user on Fedora/RHEL,  
# so there is a high chance that this ID will be equal to the current user  
# making it easier to use volumes (no permission issues)  
RUN groupadd -r jboss -g 1000 && useradd -u 1000 -r -g jboss -m -d /opt/jboss
-s /sbin/nologin -c "JBoss user" jboss && \  
chmod 755 /opt/jboss  
  
# Set the working directory to jboss' user home directory  
WORKDIR /opt/jboss  
  
# Install necessary packages  
RUN yum -y install java-1.8.0-openjdk-devel && yum clean all  
  
# Set the JAVA_HOME variable to make it clear where Java is located  
ENV JAVA_HOME /usr/lib/jvm/java  
# Specify the user which should be used to execute all commands below  
USER jboss  
  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 10.1.0.Final  
ENV WILDFLY_SHA1 9ee3c0255e2e6007d502223916cefad2a1a5e333  
ENV JBOSS_HOME /opt/jboss/wildfly  
  
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
&& rm wildfly-$WILDFLY_VERSION.tar.gz  
  
# Ensure signals are forwarded to the JVM process correctly for graceful
shutdown  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
# Expose the ports we're interested in  
EXPOSE 8080 8443  
ENV APIMAN_VERSION 1.3.1.Final  
  
RUN cd $HOME/wildfly \  
&& curl http://downloads.jboss.org/apiman/$APIMAN_VERSION/apiman-distro-
wildfly10-$APIMAN_VERSION-overlay.zip | bsdtar -xvf-  
  
ADD ./configuration/standalone-apiman.xml
/opt/jboss/wildfly/standalone/configuration/standalone-apiman.xml  
  
RUN $JBOSS_HOME/bin/add-user.sh admin admin --silent  
VOLUME /opt/jboss/wildfly/standalone/data  
  
ENTRYPOINT ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0",
"-bmanagement", "0.0.0.0", "-c", "standalone-apiman.xml"]  

