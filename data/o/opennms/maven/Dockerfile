FROM opennms/openjdk:latest  
  
LABEL maintainer "Ronny Trommer <ronny@opennms.org>"  
  
ARG MAVEN_VERSION=3.5.3  
ENV MAVEN_URL http://ftp.fau.de  
  
ENV MAVEN_PKG
${MAVEN_URL}/apache/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz  
ENV MAVEN_HOME /opt/apache-maven-${MAVEN_VERSION}  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${MAVEN_HOME}/bin  
  
LABEL license="Apache License, Version 2.0" \  
org.apache.maven.version="${MAVEN_VERSION}" \  
vendor="OpenNMS Community" \  
name="Apache Maven"  
  
WORKDIR /opt  
  
RUN curl ${MAVEN_PKG} | tar xz  

