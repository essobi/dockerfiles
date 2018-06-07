FROM cloudnesil/jetty-8-jre  
  
ENV RELIC_LOCATION /newrelic  
ENV WAR_LOCATION /opt/warfile  
##ENV WEAVER_LOCATION /opt/weaverfile  
ENV JAVA_OPTIONS -javaagent:$RELIC_LOCATION/newrelic.jar  
ENV JETTY_BASE /var/lib/jetty  
ENV JETTY_HOME /usr/local/jetty  
ENV PATH $JETTY_HOME/bin:$PATH  
RUN mkdir -p "$WAR_LOCATION"  
##RUN mkdir -p "$WEAVER_LOCATION"  
RUN mkdir -p "$RELIC_LOCATION"  
  
WORKDIR $WAR_LOCATION  
RUN wget -O kablostok.war https://s3-eu-
west-1.amazonaws.com/kablostokproject/kablostok.war  
##ADD aspectjweaver.jar $WEAVER_LOCATION/  
ADD newrelic.jar $RELIC_LOCATION/  
ADD newrelic.yml $RELIC_LOCATION/  
ADD kablostok.xml $JETTY_BASE/webapps/  
  
VOLUME $JETTY_BASE  
VOLUME $WAR_LOCATION  
VOLUME $JETTY_HOME  
##VOLUME $WEAVER_LOCATION  
EXPOSE 8080  
CMD ["jetty.sh", "run"]  

