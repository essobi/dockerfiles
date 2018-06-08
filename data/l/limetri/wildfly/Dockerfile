FROM dockerfile/java:oracle-java8  
  
MAINTAINER Timon Veenstra <timon@limetri.eu>  
  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 8.2.0.Final  
ENV HOME /opt/  
ENV KEYCLOAK_VERSION 1.0.4.Final  
  
#defaulr port offset  
ENV PORT_OFFSET 0  
# install bsdtar needed to unzip keycloak  
RUN apt-get update && apt-get install -y bsdtar  
  
# Add the WildFly distribution to /opt, and make wildfly the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN cd $HOME && curl
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar zx && mv $HOME/wildfly-$WILDFLY_VERSION $HOME/wildfly  
  
# download and unzip keycloak  
WORKDIR /opt  
RUN curl -L
https://downloads.sourceforge.net/project/keycloak/$KEYCLOAK_VERSION/keycloak-
war-dist-all-$KEYCLOAK_VERSION.zip | bsdtar -xf - && mv keycloak-war-dist-
all-$KEYCLOAK_VERSION keycloak  
WORKDIR /opt/wildfly  
RUN bsdtar -xf /opt/keycloak/adapters/keycloak-wildfly-adapter-
dist-$KEYCLOAK_VERSION.zip  
  
# Set the JBOSS_HOME env variable  
ENV JBOSS_HOME /opt/wildfly  
  
  
# Standalone.xml modifications.  
RUN sed -i -e 's/<extensions>/&\n <extension module="org.keycloak.keycloak-
wildfly-subsystem"\/>/' $JBOSS_HOME/standalone/configuration/standalone.xml &&
\  
sed -i -e 's/<profile>/&\n <subsystem
xmlns="urn:jboss:domain:keycloak:1.0"\/>/'
$JBOSS_HOME/standalone/configuration/standalone.xml && \  
sed -i -e 's/<security-domains>/&\n <security-domain name="keycloak">\n
<authentication>\n <login-module
code="org.keycloak.adapters.jboss.KeycloakLoginModule" flag="required"\/>\n
<\/authentication>\n <\/security-domain>/'
$JBOSS_HOME/standalone/configuration/standalone.xml  
  
# Create wildfly group and user, set file ownership to that user.  
RUN groupadd -r wildfly -g 433 && \  
useradd -u 431 -r -g wildfly -d /opt/wildfly -s /sbin/nologin -c "Wildfly
user" wildfly && \  
chown -R wildfly:wildfly /opt/wildfly  
  
USER wildfly  
  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
CMD ["/opt/wildfly/bin/standalone.sh", "-b",
"0.0.0.0","-Djboss.socket.binding.port-offset=$PORT_OFFSET"]  

