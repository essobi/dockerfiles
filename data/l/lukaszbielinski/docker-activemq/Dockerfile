FROM oberthur/docker-ubuntu-java:jdk8_8.91.14  
  
MAINTAINER Dawid Malinowski <d.malinowski@oberthur.com>  
  
ENV HOME=/opt/app  
ENV ACTIVEMQ_VERSION 5.13.3  
WORKDIR /opt/app  
  
ADD start-activemq.sh /bin/start-activemq.sh  
  
# Install activemq  
RUN chmod +x /bin/start-*.sh \  
&& curl -LO https://www.apache.org/dist/activemq/${ACTIVEMQ_VERSION}/apache-
activemq-${ACTIVEMQ_VERSION}-bin.tar.gz \  
&& gunzip apache-activemq-${ACTIVEMQ_VERSION}-bin.tar.gz \  
&& tar -xf apache-activemq-${ACTIVEMQ_VERSION}-bin.tar -C /opt/app \  
&& mv apache-activemq-*/ apache-activemq/ \  
&& chmod -x apache-activemq/bin/activemq \  
&& mv apache-activemq/conf/activemq.xml apache-activemq/conf/activemq.xml.orig
\  
&& awk '/.*stomp.*/{print " <transportConnector name=\"stompssl\"
uri=\"stomp+nio+ssl://0.0.0.0:61612?transport.enabledCipherSuites=SSL_RSA_WITH_RC4_128_SHA,SSL_DH_anon_WITH_3DES_EDE_CBC_SHA\"
/>"}1' apache-activemq/conf/activemq.xml.orig >> apache-
activemq/conf/activemq.xml \  
  
# change to ssl connector  
&& apt-get update \  
&& apt-get install xmlstarlet \  
&& xmlstarlet ed -L --subnode
"/_:beans/_:bean[@id='invokeConnectors']/_:property[@name='arguments']/_:list"
--type elem -n 'bean id="SecureConnector"
class="org.eclipse.jetty.server.ServerConnector"' -v "" /opt/app/apache-
activemq/conf/jetty.xml \  
&& xmlstarlet ed -L --subnode
"/_:beans/_:bean[@id='invokeConnectors']/_:property[@name='arguments']/_:list/_:bean[@id='SecureConnector'
and @class='org.eclipse.jetty.server.ServerConnector']" --type elem -n
'constructor-arg' -v "" /opt/app/apache-activemq/conf/jetty.xml \  
&& xmlstarlet ed -L --subnode
"/_:beans/_:bean[@id='invokeConnectors']/_:property[@name='arguments']/_:list/_:bean[@id='SecureConnector'
and @class='org.eclipse.jetty.server.ServerConnector']/_:constructor-arg"
--type elem -n 'bean id="handlers"
class="org.eclipse.jetty.util.ssl.SslContextFactory"' -v "" /opt/app/apache-
activemq/conf/jetty.xml \  
&& xmlstarlet ed -L --subnode
"/_:beans/_:bean[@id='invokeConnectors']/_:property[@name='arguments']/_:list/_:bean[@id='SecureConnector'
and @class='org.eclipse.jetty.server.ServerConnector']" --type elem -n
'constructor-arg ref="Server"' -v "" /opt/app/apache-activemq/conf/jetty.xml \  
&& xmlstarlet ed -L --subnode
"/_:beans/_:bean[@id='invokeConnectors']/_:property[@name='arguments']/_:list/_:bean[@id='SecureConnector'
and @class='org.eclipse.jetty.server.ServerConnector']/_:constructor-
arg/_:bean[@id='handlers']" --type elem -n 'property name="keyStorePath"
value="${activemq.conf}/broker.ks"' -v "" /opt/app/apache-
activemq/conf/jetty.xml \  
&& xmlstarlet ed -L --subnode
"/_:beans/_:bean[@id='invokeConnectors']/_:property[@name='arguments']/_:list/_:bean[@id='SecureConnector'
and @class='org.eclipse.jetty.server.ServerConnector']/_:constructor-
arg/_:bean[@id='handlers']" --type elem -n 'property name="keyStorePassword"
value="password"' -v "" /opt/app/apache-activemq/conf/jetty.xml \  
&& xmlstarlet ed -L --subnode
"/_:beans/_:bean[@id='invokeConnectors']/_:property[@name='arguments']/_:list/_:bean[@id='SecureConnector'
and @class='org.eclipse.jetty.server.ServerConnector']" --type elem -n
'property name="port" value="8162"' -v "" /opt/app/apache-
activemq/conf/jetty.xml \  
  
# clean all cache to clean space  
&& apt-get purge -y unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean \  
&& apt-get -y autoremove \  
  
&& rm apache-activemq-$ACTIVEMQ_VERSION-bin.tar  
  
ADD activemq.xml /opt/app/apache-activemq/conf/activemq.xml  
  
  
# Add user app  
RUN echo "app:x:999:999::/opt/app:/bin/false" >> /etc/passwd; \  
echo "app:x:999:" >> /etc/group; \  
mkdir -p /opt/app; chown app:app /opt/app  
  
EXPOSE 61612 61613 61616 8161 8162  
  
ENTRYPOINT ["/bin/start-activemq.sh"]  

