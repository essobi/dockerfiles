FROM dsnnimbus/oracle-java:JDK1.8.0.60  
ENV WILDFLY_VERSION 8.2.1.Final  
ENV WILDFLY_SHA1 77161d682005f26acb9d2df5548c8623ba3a4905  
ENV JBOSS_HOME /opt/jboss/wildfly  
  
RUN cd $HOME \  
&& curl -O
https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
\  
&& sha1sum wildfly-$WILDFLY_VERSION.tar.gz | grep $WILDFLY_SHA1 \  
&& tar xf wildfly-$WILDFLY_VERSION.tar.gz \  
&& mv $HOME/wildfly-$WILDFLY_VERSION $JBOSS_HOME \  
&& rm wildfly-$WILDFLY_VERSION.tar.gz  
  
USER root  
  
RUN mkdir /opt/custom && \  
mkdir /opt/custom/modules && \  
mkdir /opt/custom/others  
  
# Definindo os Volumes  
VOLUME ["/opt/custom/modules:rw", "/opt/custom/others:rw"]  
  
ENV JBOSS_MODULEPATH $JBOSS_HOME/modules:/opt/custom/modules  
  
USER jboss  
  
EXPOSE 8080  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0", "--server-config=standalone-full.xml"]  

