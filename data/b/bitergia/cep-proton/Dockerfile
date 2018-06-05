# Copyright (C) 2015 Bitergia  
# GPLv3 License  
  
FROM tomcat:7.0  
MAINTAINER Bitergia <fiware-testing@bitergia.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# download and install CEP (Proton) (service starts Automatically)  
  
RUN mkdir -p /var/lib/Proton/ProtonDefinitions && \  
cd /var/lib/Proton/ && \  
curl -OLs
https://github.com/ishkin/Proton/raw/master/artifacts/AuthoringTool.war && \  
curl -OLs
https://github.com/ishkin/Proton/raw/master/artifacts/AuthoringToolWebServer.war
&& \  
curl -OLs
https://github.com/ishkin/Proton/raw/master/artifacts/ProtonOnWebServer.war &&
\  
curl -OLs
https://github.com/ishkin/Proton/raw/master/artifacts/ProtonOnWebServerAdmin.war
&& \  
# fix configuration  
apt-get update && \  
apt-get install -y --no-install-recommends zip && \  
mkdir tmp && \  
unzip ProtonOnWebServerAdmin.war -d tmp/ && \  
cd tmp && \  
sed -e 's/$//' \  
-e 's|^\\(definitions-repository\\)=.*|\1=/var/lib/Proton/ProtonDefinitions|' \  
-i ProtonAdmin.properties && \  
zip ../ProtonOnWebServerAdmin.war * && \  
cd .. && \  
rm -rf tmp && \  
mv *.war /usr/local/tomcat/webapps/ && \  
# cleanup image  
apt-get clean && \  
apt-get autoremove --purge -y && \  
find /var/lib/apt/lists -type f -delete  
  
COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml  
  
ENV CATALINA_OPTS "-Dcom.sun.management.jmxremote
-Dcom.sun.management.jmxremote.port=8686
-Dcom.sun.management.jmxremote.ssl=false
-Dcom.sun.management.jmxremote.authenticate=false
-Djava.security.egd=file:/dev/./urandom"  
### Exposed ports  
# - App server  
EXPOSE 8080  
EXPOSE 8686  
# - Proton  
EXPOSE 3002  
EXPOSE 3302  

