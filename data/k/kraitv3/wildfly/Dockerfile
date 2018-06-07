FROM kraitv3/ubuntu-jdk:16.04-jdk8  
  
ENV WILDFLY_VERSION 12.0.0.Final  
ENV WILDFLY_SHA1 b2039cc4979c7e50a0b6ee0e5153d13d537d492f  
ENV JBOSS_HOME /opt/wildfly  
  
#Set up wildfly  
RUN cd /opt \  
&& wget
https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
\  
&& echo $WILDFLY_SHA1 wildfly-$WILDFLY_VERSION.tar.gz | sha1sum -c \  
&& tar -xvf wildfly-$WILDFLY_VERSION.tar.gz \  
&& mv /opt/wildfly-$WILDFLY_VERSION $JBOSS_HOME \  
&& rm wildfly-$WILDFLY_VERSION.tar.gz  
  
#Create admin user  
RUN $JBOSS_HOME/bin/add-user.sh admin admin --silent  
  
VOLUME $JBOSS_HOME/standalone/deployments  
  
EXPOSE 8080 8787 9990  
CMD ["/opt/wildfly/bin/standalone.sh", "--debug", "-b", "0.0.0.0",
"-bmanagement", "0.0.0.0"]

