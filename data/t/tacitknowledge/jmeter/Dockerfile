FROM openjdk:8-jre-alpine  
  
ENV JMETER_VERSION 3.2  
ENV JMETER_HOME /opt/apache-jmeter-${JMETER_VERSION}  
ENV JMETER_BIN $JMETER_HOME/bin  
ENV IP 127.0.0.1  
ENV RMI_PORT 1099  
ENV PATH $PATH:$JMETER_BIN  
ENV JAVA_MEM 512m  
WORKDIR $JMETER_HOME  
EXPOSE $RMI_PORT  
  
RUN apk add --update openssl && \  
wget https://archive.apache.org/dist/jmeter/binaries/apache-
jmeter-${JMETER_VERSION}.zip -P /tmp && \  
wget https://jmeter-plugins.org/files/packages/jpgc-json-2.6.zip -P /tmp && \  
wget https://jmeter-plugins.org/files/packages/jpgc-casutg-2.1.zip -P /tmp &&
\  
unzip -oq /tmp/apache-jmeter-${JMETER_VERSION}.zip -d /opt && \  
unzip -oq /tmp/jpgc-json-2.6.zip -d $JMETER_HOME && \  
unzip -oq /tmp/jpgc-casutg-2.1.zip -d $JMETER_HOME && \  
rm -rf /var/cache/apk/* /tmp/*.zip  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

