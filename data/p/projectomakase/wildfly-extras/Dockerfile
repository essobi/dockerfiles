FROM projectomakase/wildfly:latest  
  
MAINTAINER Richard Lucas <feedback@projectomakase.org>  
  
ENV WILDFLY_CAMEL_VERSION 3.3.0  
ENV MODESHAPE_VERSION 4.6.0.Final  
  
ENV JBOSS_HOME /opt/wildfly  
  
USER omakase  
  
#Install Wildfly-Camel  
RUN \  
cd $JBOSS_HOME && \  
curl -OL https://github.com/wildfly-extras/wildfly-
camel/releases/download/$WILDFLY_CAMEL_VERSION/wildfly-camel-
patch-$WILDFLY_CAMEL_VERSION.tar.gz && \  
tar -zxvf wildfly-camel-patch-$WILDFLY_CAMEL_VERSION.tar.gz && \  
rm wildfly-camel-patch-$WILDFLY_CAMEL_VERSION.tar.gz && \  
rm -Rf quickstarts  
  
#Install Modeshape  
RUN \  
cd $JBOSS_HOME && \  
curl -OL -nv
http://downloads.jboss.org/modeshape/$MODESHAPE_VERSION/modeshape-$MODESHAPE_VERSION-
jboss-wf9-dist.zip && \  
unzip -u modeshape-$MODESHAPE_VERSION-jboss-wf9-dist.zip && \  
rm modeshape-$MODESHAPE_VERSION-jboss-wf9-dist.zip  
  
ENTRYPOINT ["/opt/wildfly/bin/entrypoint.sh"]  
  
CMD ["/opt/wildfly/bin/standalone-docker.sh", "-c", "standalone.xml"]  

