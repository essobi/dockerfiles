FROM bitnami/tomcat:7  
MAINTAINER <mail@skoppe.eu>  
  
RUN apt-get update && \  
apt-get -y install mysql-client curl && \  
apt-get remove \--purge -y $BUILD_PACKAGES && rm -rf /var/lib/apt/lists/*

