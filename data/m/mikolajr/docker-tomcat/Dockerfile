FROM openjdk:8-jre-alpine  
MAINTAINER Mikolaj Rydzewski <mikolaj.rydzewski@gmail.com>  
  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.5.20  
ENV TOMCAT_TGZ_URL
http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz  
ENV KEYSTORE /usr/local/tomcat/conf/keystore  
ENV KEYPASS changeit  
ENV KEY_DNAME "cn=Tomcat, ou=Docker, o=cloud, c=internet"  
ADD "$TOMCAT_TGZ_URL" /usr/local/  
WORKDIR /usr/local  
RUN \  
mv apache-tomcat-${TOMCAT_VERSION}.tar.gz tomcat.tar.gz && \  
tar xzf tomcat.tar.gz && \  
mv apache-tomcat-${TOMCAT_VERSION} tomcat && \  
rm -f tomcat/bin/*.bat tomcat/bin/*.gz tomcat/temp/* tomcat.tar.gz
tomcat/[A-Z]* && \  
rm -rf tomcat/webapps/*  
  
ADD start_override.sh /usr/local/tomcat/bin/  
ADD server.xml /usr/local/tomcat/conf/  
WORKDIR /usr/local/tomcat  
EXPOSE 8009 8080 8443  
CMD [ "bin/start_override.sh", "bin/catalina.sh", "run" ]  

