# Use official Oracle Java 8 repository  
FROM openjdk:8-jre  
  
MAINTAINER Rafał Krzewski <rafal.krzewski@caltha.pl>  
  
ENV WILDFLY_VERSION 8.2.0  
# Add the WildFly distribution to /opt  
RUN curl -s
http://download.jboss.org/wildfly/${WILDFLY_VERSION}.Final/wildfly-${WILDFLY_VERSION}.Final.tar.gz
| \  
tar zx -C /opt && \  
mv /opt/wildfly-* /opt/wildfly  
  
# Create the wildfly user and group  
RUN groupadd -r wildfly -g 433 && \  
useradd -u 431 -r -g wildfly \  
-d /opt/wildfly \  
-s /sbin/nologin \  
-c "WildFly user" wildfly  
  
# Change the owner of the /opt/wildfly directory  
RUN chown -R wildfly:wildfly /opt/wildfly*  
  
# Expose the HTTP and remote control ports  
EXPOSE 8080 9990  
# Run everything below as the wildfly user  
USER wildfly  
  
# Make sure signals are passed correctly from standalone.sh to JVM  
# This ensures orderdly shutdown when docker stop is performed  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
# Run WildFly in the standalone mode and bind to public network interface  
# of the container  
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]

