FROM indigo/centos-jdk8:latest  
MAINTAINER ronny@no42.org  
  
ARG MAVEN_VERSION=3.3.9  
ENV MAVEN_URL http://ftp.halifax.rwth-aachen.de  
ENV MAVEN_PKG
${MAVEN_URL}/apache/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz  
ENV MAVEN_HOME /opt/apache-maven-${MAVEN_VERSION}  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${MAVEN_HOME}/bin  
  
WORKDIR /opt  
  
RUN curl ${MAVEN_PKG} | tar xz  

