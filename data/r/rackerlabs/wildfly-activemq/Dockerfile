# Use our wildfly 9.0.1 + postgres driver as base image  
FROM rackerlabs/wildfly-postgres  
  
# Set some needed environment variables  
ENV GITHUB_URL https://github.com/nkrendel/wildfly-docker  
ENV REPO_URL https://repository.apache.org/content/repositories/releases  
  
# Add the jboss-cli commands for ActiveMQ  
ADD commands.cli /tmp/commands.cli  
  
# Download ActiveMQ Resource Adapter from Github, Run cli and do clean-up  
RUN cd $HOME \  
&& curl -L -O $GITHUB_URL/raw/master/activemq-ra/activemq-ra.rar \  
&& mv $HOME/activemq-ra.rar $JBOSS_HOME/standalone/deployments \  
&& curl $REPO_URL/org/apache/activemq/activemq-web-console/5.11.1/activemq-
web-console-5.11.1.war -o amq-console.war \  
&& mv $HOME/amq-console.war $JBOSS_HOME/standalone/deployments \  
&& $JBOSS_HOME/bin/jboss-cli.sh --file=/tmp/commands.cli \  
&& rm -rf $JBOSS_HOME/standalone/configuration/standalone_xml_history  
  
# Add ActiveMQ Web Console related properties to standalone.sh  
RUN sed -i -e "s/SERVER_OPTS=\"\"/SERVER_OPTS=\"-Dwebconsole.type=properties
-Dwebconsole.jms.url=tcp:\/\/localhost:61616
-Dwebconsole.jmx.url=service:jmx:http-remoting-jmx:\/\/localhost:9990\"/"
$JBOSS_HOME/bin/standalone.sh  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990  
# Set the default entrypoint to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
ENTRYPOINT ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0",
"-bmanagement", "0.0.0.0"]  
CMD ["-Dactivemq.data=wildfly/standalone/data/activemq"]  

