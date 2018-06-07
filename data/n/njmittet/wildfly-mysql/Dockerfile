FROM njmittet/alpine-wildfly:10.1.0.Final  
  
ENV CONNECTOR_VERSION mysql-connector-java-5.1.40  
RUN mkdir -p /opt/jboss/wildfly/modules/com/mysql/main  
RUN curl -O -L
https://dev.mysql.com/get/Downloads/Connector-J/$CONNECTOR_VERSION.zip \  
&& unzip $CONNECTOR_VERSION.zip \  
&& mv $CONNECTOR_VERSION/$CONNECTOR_VERSION-bin.jar
/opt/jboss/wildfly/modules/com/mysql/main/$CONNECTOR_VERSION.jar \  
&& rm -r $CONNECTOR_VERSION && rm $CONNECTOR_VERSION.zip  
COPY module.xml /opt/jboss/wildfly/modules/com/mysql/main/module.xml  

