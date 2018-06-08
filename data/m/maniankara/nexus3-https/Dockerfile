FROM java:8  
MAINTAINER Anoop Vijayan Maniankara<maniankara@gmail.com>  
  
# Env variables  
ENV NEXUS_HOME=/opt/sonatype/nexus \  
NEXUS_VERSION=3.0.0-03 \  
NEXUS_DOMAIN=example.com \  
NEXUS_IP_ADDRESS=173.168.1.1 \  
SONATYPE_WORK=/sonatype-work  
  
# Create nexus user  
RUN useradd -r -u 200 -m -c "nexus role account" -d ${SONATYPE_WORK} nexus  
  
# Download and install nexus  
ADD http://download.sonatype.com/nexus/3/nexus-$NEXUS_VERSION-unix.tar.gz
/opt/nexus.tar.gz  
RUN mkdir -p /opt/sonatype && \  
tar zxf /opt/nexus.tar.gz -C /tmp/ && \  
mv /tmp/nexus-$NEXUS_VERSION $NEXUS_HOME && \  
chown -R nexus:nexus $NEXUS_HOME  
  
# Generate the keystore  
RUN ${JAVA_HOME}/bin/keytool -genkeypair -keystore /tmp/server-keystore.jks
-storepass changeit -keypass changeit -alias jetty -keyalg RSA -keysize 2048
-validity 5000 -dname "CN=*.${NEXUS_DOMAIN}, OU=Example, O=Sonatype,
L=Unspecified, ST=Unspecified, C=US" -ext
"SAN=DNS:${NEXUS_DOMAIN},IP:${NEXUS_IP_ADDRESS}" -ext "BC=ca:true" && \  
  
# Copy the generated keystore to the KeyStorePath  
mkdir -p $NEXUS_HOME/etc/ssl/ && \  
cp /tmp/server-keystore.jks $NEXUS_HOME/etc/ssl/keystore.jks && \  
  
# Add it to the ssl-port  
echo "application-port-ssl=8443" >> $NEXUS_HOME/etc/org.sonatype.nexus.cfg &&
\  
  
# Change the path in the SSLContextFactory  
sed -i 's%^.*KeyStorePassword.*$%\<Set
name="KeyStorePassword"\>changeit\<\/Set\>%' $NEXUS_HOME/etc/jetty-https.xml
&& \  
sed -i 's%^.*KeyManagerPassword.*$%\<Set
name="KeyManagerPassword"\>changeit\<\/Set\>%' $NEXUS_HOME/etc/jetty-https.xml
&& \  
sed -i 's%^.*TrustStorePassword.*$%\<Set
name="TrustStorePassword"\>changeit\<\/Set\>%' $NEXUS_HOME/etc/jetty-https.xml
&& \  
  
# Update the cfg file with the changes  
sed -i 's%^nexus-args.*$%nexus-
args=\${karaf.etc}/jetty.xml,\${karaf.etc}\/jetty-
http.xml,\${karaf.etc}\/jetty-requestlog.xml,\${karaf.etc}\/jetty-
https.xml,\${karaf.etc}\/jetty-http-redirect-to-https.xml%'
$NEXUS_HOME/etc/org.sonatype.nexus.cfg  
  
  
# Switch to nexus user  
USER nexus  
  
# nexus workdir  
WORKDIR $NEXUS_HOME  
  
# data volume for external mounts  
VOLUME ["$NEXUS_HOME/data"]  
  
# http and https ports  
EXPOSE 8081 8443  
# launch  
CMD ["/opt/sonatype/nexus/bin/nexus", "run-redirect"]  

