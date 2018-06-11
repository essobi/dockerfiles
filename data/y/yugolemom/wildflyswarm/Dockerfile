FROM openshift/base-centos7  
  
MAINTAINER Hugo C. Lima <yugolemom@gmail.com>  
  
ENV MAVEN_VERSION 3.3.9  
LABEL io.k8s.description="JEE - WildFly Swarm" \  
io.k8s.display-name="WildFly Swarm" \  
io.openshift.expose-services="8080:http,8888:ping" \  
io.openshift.tags="builder,wildflyswarm" \  
io.openshift.s2i.destination="/tmp"  
  
# Install Maven  
RUN yum install -y --enablerepo=centosplus \  
tar unzip bc which lsof java-1.8.0-openjdk java-1.8.0-openjdk-devel && \  
yum clean all -y && \  
(curl -0
https://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | \  
tar -zx -C /usr/local) && \  
ln -sf /usr/local/apache-maven-$MAVEN_VERSION/bin/mvn /usr/local/bin/mvn  
  
COPY .s2i/bin/ $STI_SCRIPTS_PATH  
  
ENV JAVA_OPTIONS -Xmx512m  
  
USER 1001  
EXPOSE 8080  

