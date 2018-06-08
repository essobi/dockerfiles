FROM nibo/oracle-jdk:jdk-8u112  
MAINTAINER Richard <nibocn@gmail.com>  
  
ARG MAVEN_VERSION=3.3.9  
  
RUN mkdir -p /opt/maven \  
&& curl -fsSL
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
| tar -xzC /opt/maven --strip-components=1 \  
&& ln -s /opt/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /opt/maven

