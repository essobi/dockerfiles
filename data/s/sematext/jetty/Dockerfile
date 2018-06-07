FROM sematext/jdk-oracle  
  
ENV APP_ROOT /opt/jetty  
  
ENV JETTY_VERSION 9.4.8.v20171121  
ENV JETTY_URL https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-
home/$JETTY_VERSION/jetty-home-$JETTY_VERSION.tar.gz  
  
RUN \  
curl -fSL "$JETTY_URL" -o /tmp/jetty.tar.gz && \  
tar -xvf /tmp/jetty.tar.gz -C /opt && \  
mv "${APP_ROOT}-home-${JETTY_VERSION}" "$APP_ROOT" && \  
rm /tmp/jetty.tar.gz  

