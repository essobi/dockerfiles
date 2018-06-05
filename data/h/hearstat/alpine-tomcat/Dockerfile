FROM hearstat/alpine-java:jdk8  
  
MAINTAINER Hearst Automation Team <atat@hearst.com>  
  
ENV TOMCAT_VERSION 7.0.65  
ENV TOMCAT_URL
https://archive.apache.org/dist/tomcat/tomcat-7/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz  
  
RUN apk add --update \  
tar \  
&& rm /var/cache/apk/*  
  
# SET CATALINE_HOME and PATH  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
RUN mkdir -p $CATALINA_HOME\  
&& addgroup tomcat\  
&& adduser -h $CATALINA_HOME -D -s /bin/bash -G tomcat tomcat\  
&& set -x \  
&& cd $CATALINA_HOME\  
&& curl -fSL "$TOMCAT_URL" -o tomcat.tar.gz \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& chown -R tomcat:tomcat $CATALINA_HOME\  
&& chmod -R g-s /opt\  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz* \  
&& rm -rf webapps/*  
  
USER tomcat  
  
WORKDIR $CATALINA_HOME  
  
EXPOSE 8080  

