FROM java:8-jdk-alpine  
  
ENV JMETER_VERSION=3.0  
ENV INSTALL_LOCATION=/usr/local  
  
ENV JMETER_BINARY=$INSTALL_LOCATION/jmeter/bin/jmeter  
  
# Install JMeter  
RUN cd $INSTALL_LOCATION && \  
wget http://www.mirrorservice.org/sites/ftp.apache.org/jmeter/binaries/apache-
jmeter-${JMETER_VERSION}.tgz && \  
tar xzf apache-jmeter-$JMETER_VERSION.tgz && \  
rm -f apache-jmeter-$JMETER_VERSION.tgz && \  
mv apache-jmeter-$JMETER_VERSION jmeter  
  
ENV JMETER_PLUGINS_VERSION=1.4.0  
RUN cd $INSTALL_LOCATION/jmeter && \  
wget http://jmeter-plugins.org/downloads/file/JMeterPlugins-
Standard-${JMETER_PLUGINS_VERSION}.zip && \  
wget http://jmeter-plugins.org/downloads/file/JMeterPlugins-
Extras-${JMETER_PLUGINS_VERSION}.zip && \  
wget http://jmeter-plugins.org/downloads/file/JMeterPlugins-
ExtrasLibs-${JMETER_PLUGINS_VERSION}.zip && \  
unzip -o JMeterPlugins-Standard-${JMETER_PLUGINS_VERSION}.zip && \  
unzip -o JMeterPlugins-Extras-${JMETER_PLUGINS_VERSION}.zip && \  
unzip -o JMeterPlugins-ExtrasLibs-${JMETER_PLUGINS_VERSION}.zip  
  
ENV CONSUL_TEMPLATE_VERSION=0.14.0  
RUN cd $INSTALL_LOCATION/bin && \  
wget https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip  
  
RUN cd $INSTALL_LOCATION/jmeter/lib/ext && \  
wget https://github.com/ynaa/JMeter-
WebSocketSampler/releases/download/version-1.0.2/JMeterWebSocketSampler-1.0.2-SNAPSHOT.jar
&& \  
wget http://central.maven.org/maven2/org/eclipse/jetty/websocket/websocket-
server/9.1.1.v20140108/websocket-server-9.1.1.v20140108.jar && \  
wget http://central.maven.org/maven2/org/eclipse/jetty/jetty-
io/9.1.1.v20140108/jetty-io-9.1.1.v20140108.jar && \  
wget http://central.maven.org/maven2/org/eclipse/jetty/jetty-
util/9.1.1.v20140108/jetty-util-9.1.1.v20140108.jar && \  
wget http://central.maven.org/maven2/org/eclipse/jetty/websocket/websocket-
api/9.1.1.v20140108/websocket-api-9.1.1.v20140108.jar && \  
wget http://central.maven.org/maven2/org/eclipse/jetty/websocket/websocket-
client/9.1.1.v20140108/websocket-client-9.1.1.v20140108.jar && \  
wget http://central.maven.org/maven2/org/eclipse/jetty/websocket/websocket-
common/9.1.1.v20140108/websocket-common-9.1.1.v20140108.jar  
  
RUN mkdir -p /etc/consul-template/config.d /etc/consul-template/template.d
/tests  
  
#ENV CONSUL_WAIT=5s:20s  
#This presumes that container is running at --net=host, which is a good idea
re RMI anyway  
ENV CONSUL_HOST=127.0.0.1:8500  
ADD jmeter-master-start.sh.tmpl /  
  
ENV START_SCRIPT=jmeter-server-start.sh  
  
ENV RMI_HOST=0.0.0.0  
ENTRYPOINT ["consul-template", "-wait", "5s:20s", "-consul",
"consul.service.consul:8500", "-template", \  
"/jmeter-master-start.sh.tmpl:/jmeter-master-start.sh:killall java; sh
/jmeter-master-start.sh &"]  
  
# to run/test:  
# docker build -t jmeter . && docker run -it --rm --net host -e
CONSUL_WAIT="0s" -e CONSUL_HOST=x.x.x.x:8500 jmeter  
#Running in AWS:  
#https://gist.github.com/warnergodfrey/8037420

