FROM jboss/wildfly:9.0.2.Final  
MAINTAINER Jorge Morales <jmorales@redhat.com>  
  
ENV APIMAN_VERSION 1.2.1.Final  
  
RUN cd $JBOSS_HOME \  
&& curl http://downloads.jboss.org/overlord/apiman/$APIMAN_VERSION/apiman-
distro-wildfly9-$APIMAN_VERSION-overlay.zip -o apiman-distro-
wildfly9-$APIMAN_VERSION-overlay.zip \  
&& bsdtar -xf apiman-distro-wildfly9-$APIMAN_VERSION-overlay.zip \  
&& rm apiman-distro-wildfly9-$APIMAN_VERSION-overlay.zip  
  
ENTRYPOINT ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-c",
"standalone-apiman.xml"]  
  

