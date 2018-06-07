FROM tomcat:8-jre8  
  
MAINTAINER David Milward <david@metadataconsulting.co.uk>  
  
ENV MC_VERSION 2.1.35  
ENV MC_WAR_URL
https://github.com/MetadataRegistry/ModelCataloguePlugin/releases/download/$MC_VERSION/mc.war  
ENV MC_CONFIG_URL
https://github.com/MetadataRegistry/ModelCataloguePlugin/releases/download/$MC_VERSION/mc-
config.groovy  
  
LABEL Description="This image is used to run Metadata Registry inside Docker"
Vendor="Metadata Consulting Ltd." Version="$MC_VERSION"  
  
RUN set -x \  
&& rm -rf /usr/local/tomcat/webapps/ROOT \  
&& rm -rf /usr/local/tomcat/webapps/manager \  
&& rm -rf /usr/local/tomcat/webapps/docs \  
&& rm -rf /usr/local/tomcat/webapps/examples \  
&& rm -rf /usr/local/tomcat/webapps/host-manager \  
&& curl -fSL "$MC_WAR_URL" -o /usr/local/tomcat/webapps/ROOT.war \  
&& curl -fSL "$MC_CONFIG_URL" -o /usr/local/tomcat/conf/mc-config.groovy  
  
EXPOSE 8080  

