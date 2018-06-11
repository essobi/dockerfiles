FROM njmittet/alpine-openjdk:jre8  
  
MAINTAINER Nils Jørgen Mittet <njmittet@gmail.com>  
  
ENV WILDFLY_VERSION 10.1.0.Final  
ENV JBOSS_HOME /opt/jboss/wildfly  
ENV STANDALONE standalone  
  
USER root  
RUN mkdir -p /opt/jboss && adduser -D -h /opt/jboss jboss && apk update && apk
add curl && rm -rf /var/cache/apk/*  
  
USER jboss  
WORKDIR /opt/jboss  
RUN curl -O
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.zip
&& unzip wildfly-$WILDFLY_VERSION.zip && mv $HOME/wildfly-$WILDFLY_VERSION
$HOME/wildfly && rm wildfly-$WILDFLY_VERSION.zip  
  
EXPOSE 8080 9990  
CMD /opt/jboss/wildfly/bin/standalone.sh --server-config=$STANDALONE.xml -b
0.0.0.0  

