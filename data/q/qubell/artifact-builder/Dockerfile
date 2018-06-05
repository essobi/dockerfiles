FROM java:openjdk-7-jdk  
MAINTAINER Nikolay Sokolov <nsokolov@tonomi.com>  
  
ENV MAVEN_VERSION 3.3.3  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
VOLUME /root/.m2  
VOLUME /source  
  
WORKDIR /source  
  
ENV MAVEN_HOME /usr/share/maven  
ENV ARTIFACT_PATTERN "*.war"  
ENV PUBLISH_PATH application.war  
  
ADD run.sh /run.sh  
  
EXPOSE 80  
CMD /run.sh  

