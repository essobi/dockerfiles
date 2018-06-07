FROM debian:stretch  
  
ARG GUACAMOLE_VERSION="0.9.14"  
ENV GUACAMOLE_HOME=/config  
  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qy \  
ca-certificates \  
gosu \  
libservlet3.1-java \  
libtcnative-1 \  
tomcat8 \  
wget \  
xfonts-terminus && \  
wget -qO /var/lib/tomcat8/webapps/guacamole.war
"http://apache.org/dyn/closer.cgi?action=download&filename=guacamole/${GUACAMOLE_VERSION}/binary/guacamole-${GUACAMOLE_VERSION}.war"
&& \  
rm -r /var/lib/tomcat8/webapps/ROOT && \  
sed -i 's/^\(common.loader=.*\)/#\1/g' /etc/tomcat8/catalina.properties && \  
sed -i 's/^\(server.loader=.*\)/#\1/g' /etc/tomcat8/catalina.properties && \  
sed -i 's/^\(shared.loader=.*\)/#\1/g' /etc/tomcat8/catalina.properties && \  
echo
'common.loader="${catalina.base}/lib","${catalina.base}/lib/*.jar","${catalina.home}/lib","${catalina.home}/lib/*.jar"'
>> /etc/tomcat8/catalina.properties && \  
DEBIAN_FRONTEND=noninteractive apt-get purge -qq \  
wget && \  
DEBIAN_FRONTEND=noninteractive apt-get -y autoremove --purge && \  
DEBIAN_FRONTEND=noninteractive apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
useradd -r -u 911 -U -d /config -s /bin/false abc && \  
usermod -G users abc && \  
chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

