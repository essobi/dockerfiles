FROM centos  
  
MAINTAINER <contato@eduardomedeiros.me>  
  
# Expose the ports  
EXPOSE 8080  
EXPOSE 9990  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 12.0.0.Final  
  
# Add user and group wildfly  
RUN groupadd wildfly  
RUN adduser -g wildfly wildfly  
  
# Install JDK 8  
RUN yum install java-1.8.0-openjdk-devel -y  
  
# Download and install WildFly  
RUN curl -O
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz  
RUN tar xzvf wildfly-$WILDFLY_VERSION.tar.gz -C /opt  
RUN ln -s /opt/wildfly-$WILDFLY_VERSION /opt/wildfly  
RUN chown -R wildfly:wildfly /opt/wildfly-$WILDFLY_VERSION  
  
# Add user admin / pass: wildfly  
USER wildfly  
RUN /opt/wildfly/bin/add-user.sh admin wildfly --silent  
  
# Deploy  
USER wildfly  
ADD hello.war /opt/wildfly/standalone/deployments/  
  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
USER wildfly  
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"]  

