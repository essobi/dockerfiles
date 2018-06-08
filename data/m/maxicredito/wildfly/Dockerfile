FROM maxicredito/openjdk:8-alpine  
  
MAINTAINER Carlos Bittarello <cbittarello@gmail.com>  
  
ENV WILDFLY_VERSION 13.0.0.Final  
  
ENV JBOSS_HOME /opt/wildfly  
  
RUN cd $HOME && mkdir /opt && mkdir /opt/wildfly && \  
addgroup -g 1000 -S wildfly && \  
adduser -u 1000 -S wildfly -G wildfly && \  
wget -q
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
&& \  
tar xzvf wildfly-$WILDFLY_VERSION.tar.gz && \  
mv -f $HOME/wildfly-$WILDFLY_VERSION/* $JBOSS_HOME && \  
rm -rf wildfly-$WILDFLY_VERSION.tar.gz && \  
chown -R wildfly:0 ${JBOSS_HOME} && \  
chmod -R g+rw ${JBOSS_HOME}  
  
USER wildfly  
  
ENV JAVA_OPTS ''  
  
EXPOSE 8080  
  
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]

