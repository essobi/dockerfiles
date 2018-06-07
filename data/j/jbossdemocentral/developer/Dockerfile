# Use latest jboss/base-jdk:8 image as the base  
FROM jboss/base-jdk:8  
# Maintainer details  
MAINTAINER Andrew Block <andy.block@gmail.com>  
  
# Switch to root to perform installations  
USER root  
  
# Maven version  
ENV MAVEN_VERSION 3.2.5  
# Update Sudoers, Install dependencies and add required directories  
RUN echo 'jboss ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers \  
&& yum install -y wget sudo unzip git apr-devel \  
&& yum clean all \  
&& curl -sSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \  
&& mkdir /opt/jboss/.m2 \  
&& chown -R 1000:1000 /opt/jboss/.m2  
  
# Maven home  
ENV M2_HOME /usr/share/maven  
  
# Add custom Maven Settings file  
ADD support/settings.xml /opt/jboss/.m2/settings.xml  
  
# Modify permissions on Maven settings file  
RUN chown jboss:jboss /opt/jboss/.m2/settings.xml  
  
# Run as user JBoss  
USER 1000  

