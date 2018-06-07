FROM indigolabs/base:tomcat8  
MAINTAINER Nicolas Seigneur <nseigneur@indigoconsulting.ca>  
  
#Create Base folder for Configurator and Admin Tools  
RUN mkdir -p /opt/forgerock/openam/ssoadm/; mkdir
/opt/forgerock/openam/configurator/  
  
#Download the Configurator tools, extract and remove source  
RUN wget --quiet
http://maven.forgerock.org/repo/repo/org/forgerock/openam/openam-distribution-
ssoconfiguratortools/13.0.0/openam-distribution-
ssoconfiguratortools-13.0.0.zip \  
&& unzip -q -o openam-distribution-ssoconfiguratortools-13.0.0.zip -d
/opt/forgerock/openam/configurator/ \  
&& rm -rf openam-distribution-ssoconfiguratortools-13.0.0.zip  
  
#Download Admin Tool, extract and remove source  
RUN wget --quiet
http://maven.forgerock.org/repo/snapshots/org/forgerock/openam/openam-
distribution-ssoadmintools/13.0.0-SNAPSHOT/openam-distribution-
ssoadmintools-13.0.0-20160112.160558-852.zip \  
&& unzip -q -o openam-distribution-
ssoadmintools-13.0.0-20160112.160558-852.zip -d /opt/forgerock/openam/ssoadm \  
&& rm -rf openam-distribution-ssoadmintools-13.0.0-20160112.160558-852.zip  
  
#Download WAR file  
RUN wget --quiet --output-document=/opt/tomcat/webapps/openam.war
http://maven.forgerock.org/repo/snapshots/org/forgerock/openam/openam-
server/13.0.0-SNAPSHOT/openam-server-13.0.0-20160112.160558-885.war  

