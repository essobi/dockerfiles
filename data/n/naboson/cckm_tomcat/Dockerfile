FROM java:8-jdk  
  
ENV TOMCAT_FAMILY 8  
ENV TOMCAT_VERSION 8.0.35  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y vim wget maven  
  
# Get Tomcat  
RUN wget --quiet --no-cookies
http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_FAMILY}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/tomcat.tgz  
  
# Uncompress  
RUN tar xzvf /tmp/tomcat.tgz -C /opt  
RUN mv /opt/apache-tomcat-${TOMCAT_VERSION} /opt/tomcat  
RUN rm /tmp/tomcat.tgz  
  

