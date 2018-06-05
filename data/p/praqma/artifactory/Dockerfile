FROM tomcat:8.0.41-jre8-alpine  
  
MAINTAINER Hans G, Praqma  
  
ENV ARTIFACTORY_VERSION 5.1.4  
RUN apk add --update openssl && apk add --update unzip  
  
RUN rm -rf webapps/  
  
RUN wget -O artifactory.zip
https://bintray.com/jfrog/artifactory/download_file?file_path=jfrog-
artifactory-oss-${ARTIFACTORY_VERSION}.zip \  
&& unzip -j artifactory.zip "artifactory-*/webapps/artifactory.war" -d
webapps/  
  
COPY config/context.xml /usr/local/tomcat/conf/  
RUN mkdir -p webapps/ROOT/WEB-INF  
COPY config/rewrite.config /usr/local/tomcat/webapps/ROOT/WEB-INF/  
  
RUN mkdir -p /artifactory  
ENV ARTIFACTORY_HOME /artifactory  
  
WORKDIR /artifactory  

