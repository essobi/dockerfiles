FROM dockerfile/java:oracle-java8  
MAINTAINER Eduardo Souza  
  
#  
# wildfly  
#  
ENV WILDFLY_VERSION 8.2.0.Final  
  
# Create the wildfly user and group  
RUN \  
groupadd -r wildfly -g 433 && \  
useradd -u 431 -r -g wildfly -d /opt/wildfly -s /sbin/nologin -c "WildFly
user" wildfly && \  
mkdir /opt/wildfly-$WILDFLY_VERSION && \  
apt-get -y install curl && \  
cd /opt && \  
curl
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar zx && \  
chown -R wildfly:wildfly /opt/wildfly-$WILDFLY_VERSION && \  
ln -s /opt/wildfly-$WILDFLY_VERSION /opt/wildfly && \  
chown -R wildfly:wildfly /opt/wildfly  
  
# Add admin user  
RUN /opt/wildfly/bin/add-user.sh admin admin123_ --silent  
  
# Set the JBOSS_HOME env variable  
ENV JBOSS_HOME /opt/wildfly  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990  
# Run everything below as the wildfly user  
USER wildfly  
  
# command to run at boot  
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"]  

