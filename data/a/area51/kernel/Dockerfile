FROM area51/java:serverjre-8  
MAINTAINER Peter Mount <peter@retep.org>  
  
ENV KERNEL_LIB /opt/kernel  
  
ENV KERNEL_VERSION 1.0-SNAPSHOT  
ENV MAVEN_VERSION 3.3.9  
  
RUN mkdir -p /opt/kernel &&\  
cd /tmp &&\  
curl -sSL \  
-o maven.zip \  
https://repo.maven.apache.org/maven2/org/apache/maven/apache-
maven/${MAVEN_VERSION}/apache-maven-${MAVEN_VERSION}-bin.zip &&\  
unzip maven.zip &&\  
/tmp/*maven*/bin/mvn \  
-Dmaven.repo.local=/tmp/repo \  
org.apache.maven.plugins:maven-dependency-plugin:2.10:get \  
-DrepoUrl=https://nexus.area51.onl/repository/maven-public \  
-Dartifact=onl.area51.kernel:generic-image:${KERNEL_VERSION}:tar:assembly \  
-Dtransitive=false &&\  
cd /opt &&\  
tar xvf /tmp/repo/onl/area51/kernel/generic-image/${KERNEL_VERSION}/generic-
image-${KERNEL_VERSION}-assembly.tar &&\  
rm -rf /tmp/*  
  
CMD ["/opt/kernel/start"]  
  

