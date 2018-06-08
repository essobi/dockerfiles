FROM ubuntu:14.04  
MAINTAINER Alex Guzun "alex@aguzun.com"  
RUN sudo apt-get update  
RUN sudo apt-get install software-properties-common python-software-properties
-y  
RUN sudo add-apt-repository ppa:webupd8team/java  
RUN sudo apt-get update  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN sudo apt-get install oracle-java8-set-default oracle-java8-installer -y  
  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 9.0.1.Final  
  
# Add the WildFly distribution to /opt  
RUN cd /opt && wget
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz  
RUN cd /opt && tar xvf wildfly-$WILDFLY_VERSION.tar.gz && rm
wildfly-$WILDFLY_VERSION.tar.gz  
  
# Make sure the distribution is available from a well-known place  
RUN ln -s /opt/wildfly-$WILDFLY_VERSION /opt/wildfly  
  
# Set the JBOSS_HOME env variable  
ENV JBOSS_HOME /opt/wildfly  
  
# Create the wildfly user and group  
RUN groupadd -r wildfly -g 433 && useradd -u 431 -r -g wildfly -d /opt/wildfly
-s /bin/false -c "WildFly user" wildfly  
  
# Change the owner of the /opt/wildfly directory  
RUN chown -R wildfly:wildfly /opt/wildfly*  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990  
# Run everything below as the wildfly user  
USER wildfly  
  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"]

