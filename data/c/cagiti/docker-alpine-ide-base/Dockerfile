FROM java:8-jdk-alpine  
MAINTAINER Cai Cooper "caicooper82@gmail.com"  
ENV MAVEN_VERSION 3.5.0  
ENV MAVEN_HOME /opt/maven  
ENV M2_HOME /opt/maven  
ENV M2 /opt/maven/bin  
ENV PATH ${PATH}:${M2}  
  
RUN addgroup -g 1000 developer \  
&& adduser -h /home/developer -u 1000 -G developer -s /bin/bash -D developer  
  
RUN apk update && apk --no-cache add gtk+3.0 libcanberra-gtk3 curl libxext-dev
libxrender-dev libxtst-dev ttf-dejavu gnome-vfs git libgnome-dev && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir -p /opt /root/.m2 && \  
curl -L /tmp/apache-maven-${MAVEN_VERSION}.tar.gz
http://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz | tar -zx -C /opt && \  
ln -s /opt/apache-maven-${MAVEN_VERSION} ${MAVEN_HOME} && \  
ln -s ${MAVEN_HOME}/bin/mvn /usr/local/bin && \  
ln -s /opt/maven/conf/settings.xml ~/.m2/ && \  
rm -f /tmp/apache-maven-${MAVEN_VERSION}.tar.gz  

