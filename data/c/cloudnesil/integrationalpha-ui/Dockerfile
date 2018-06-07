FROM cloudnesil/jetty-7-jre  
  
ENV RELIC_LOCATION /newrelic  
ENV WAR_LOCATION /opt/warfile  
ENV JAVA_OPTIONS -javaagent:$RELIC_LOCATION/newrelic.jar  
ENV JETTY_BASE /var/lib/jetty  
ENV JETTY_HOME /usr/local/jetty  
ENV PATH $JETTY_HOME/bin:$PATH  
RUN mkdir -p "$WAR_LOCATION"  
RUN mkdir -p "$RELIC_LOCATION"  
  
WORKDIR $WAR_LOCATION  
RUN wget https://s3-eu-
west-1.amazonaws.com/integrationalphaproject/integrationalphaui.war  
ADD newrelic.jar $RELIC_LOCATION/  
ADD newrelic.yml $RELIC_LOCATION/  
  
WORKDIR $JETTY_BASE/webapps  
RUN wget https://s3-eu-
west-1.amazonaws.com/integrationalphaproject/integrationalphaui.xml  
  
VOLUME $JETTY_BASE  
VOLUME $WAR_LOCATION  
VOLUME $JETTY_HOME  
  
EXPOSE 8080  
CMD ["jetty.sh", "run"]

