FROM hedlund/java:6  
MAINTAINER henrik@hedlund.im  
  
ENV JETTY_HOME /opt/jetty  
ENV JETTY_VERSION 8.1.17.v20150415  
ENV PATH $JETTY_HOME/bin:$PATH  
  
RUN wget http://download.eclipse.org/jetty/${JETTY_VERSION}/dist/jetty-
distribution-${JETTY_VERSION}.zip -O /tmp/jetty.zip  
  
# Unpack  
RUN cd /opt && jar xf /tmp/jetty.zip  
RUN ln -s /opt/jetty-distribution-${JETTY_VERSION} /opt/jetty  
RUN rm /tmp/jetty.zip  
  
RUN chmod a+x $JETTY_HOME/bin/jetty.sh  
  
# Add custom configuration  
ADD start.ini $JETTY_HOME/  
ADD jetty-logging.xml $JETTY_HOME/etc/  
ADD jetty-jndi.xml $JETTY_HOME/etc/  
  
WORKDIR /opt/jetty/bin  
  
EXPOSE 8080 8778  
ENTRYPOINT ["jetty.sh", "run"]

