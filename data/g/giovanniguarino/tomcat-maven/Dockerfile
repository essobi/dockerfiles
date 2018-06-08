FROM ubuntu:latest  
  
MAINTAINER Giovanni Guarino <giovanniguarino.com@gmail.com>  
  
ENV TOMCAT_VERSION 8.0.32  
# Set locales  
RUN locale-gen en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
ENV LC_CTYPE en_GB.UTF-8  
# Fix sh  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install dependencies  
RUN apt-get update && \  
apt-get install -y git build-essential curl wget software-properties-common  
  
# Install JDK 8  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer wget unzip tar && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Install Maven  
RUN apt-add-repository universe  
RUN apt-get update  
RUN apt-get install -y maven  
  
# Get Tomcat  
RUN wget --quiet --no-cookies
http://apache.rediris.es/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/tomcat.tgz && \  
tar xzvf /tmp/tomcat.tgz -C /opt && \  
mv /opt/apache-tomcat-${TOMCAT_VERSION} /opt/tomcat  
  
# Define CATALINA variable  
ENV CATALINA_HOME /opt/tomcat  
ENV CATALINA_BASE /opt/tomcat  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
# Expose port 8080 8009  
EXPOSE 8080  
EXPOSE 8009  
WORKDIR $CATALINA_HOME  
  
# Start Tomcat  
CMD ["catalina.sh", "run"]  

