FROM jboss/wildfly:8.2.0.Final  
MAINTAINER Jorge Morales <jmorales@redhat.com>  
  
ENV APIMAN_VERSION 1.1.9.Final  
  
RUN cd $JBOSS_HOME \  
&& curl http://downloads.jboss.org/overlord/apiman/$APIMAN_VERSION/apiman-
distro-wildfly8-$APIMAN_VERSION-overlay.zip -o apiman-distro-
wildfly8-$APIMAN_VERSION-overlay.zip \  
&& bsdtar -xf apiman-distro-wildfly8-$APIMAN_VERSION-overlay.zip \  
&& rm apiman-distro-wildfly8-$APIMAN_VERSION-overlay.zip  
  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-c",
"standalone-apiman.xml"]  
  

