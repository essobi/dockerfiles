FROM jenkins:latest  
  
USER root  
  
ENV MAVEN_VERSION=3.3.9  
ENV MAVEN_FILE=apache-maven-$MAVEN_VERSION-bin.tar.gz  
ENV MAVEN_HOME=/usr/share/maven  
  
RUN mkdir -p $MAVEN_HOME $MAVEN_HOME/ref \  
&& curl -fsSL
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/$MAVEN_FILE \  
| tar -xzC $MAVEN_HOME \--strip-components=1 \  
&& ln -s $MAVEN_HOME/bin/mvn /usr/bin/mvn  
  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
  
USER jenkins  

