FROM tiredofit/tomcat:8-latest  
LABEL maintainer="Dave Conroy (dave at tiredofit dot ca)"  
### Install Dependencies  
RUN apk update && \  
apk add \  
mariadb-client \  
unzip \  
wget && \  
  
### Install MariaDB Java Connector  
curl -SlLo /usr/local/tomcat/lib/mariadb-java-client-2.1.0.jar
https://downloads.mariadb.com/Connectors/java/connector-java-2.1.0/mariadb-
java-client-2.1.0.jar && \  
  
### Download Orbeon and Unpack  
cd /usr/src && \  
wget https://github.com/orbeon/orbeon-forms/releases/download/tag-
release-2017.1-ce/orbeon-2017.1.201706222342-CE.zip && \  
unzip -d . orbeon-2017.1.201706222342-CE.zip && \  
mkdir -p /usr/local/tomcat/webapps/orbeon && \  
cp -R /usr/src/orbeon-2017.1.201706222342-CE/orbeon.war
/usr/local/tomcat/webapps/orbeon/ && \  
cd /usr/local/tomcat/webapps/orbeon/ && \  
unzip -d . orbeon.war && \  
rm -rf orbeon.war && \  
rm -rf /usr/src/* && \  
rm -rf /usr/local/tomcat/webapps/docs /usr/local/tomcat/webapps/docs
/usr/local/tomcat/webapps/examples /usr/local/tomcat/webapps/host-manager
/usr/local/tomcat/webapps/manager && \  
  
### Cleanup  
apk del \  
unzip \  
wget && \  
  
rm -rf /var/cache/apk/*  
  
### Add Files  
ADD install /  

