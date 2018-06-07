FROM java:8-jdk-alpine  
  
ENV \  
MAVEN_VERSION=3.3.9 \  
MAVEN_HOME=/usr/local/maven  
  
RUN \  
cd /usr/local && \  
apk add --no-cache wget bash && \  
wget https://repo1.maven.org/maven2/org/apache/maven/apache-
maven/$MAVEN_VERSION/apache-maven-$MAVEN_VERSION-bin.zip && \  
unzip apache-maven-$MAVEN_VERSION-bin.zip && \  
rm -f apache-maven-$MAVEN_VERSION-bin.zip && \  
ln -s apache-maven-$MAVEN_VERSION maven && \  
apk del wget  
  
ENV PATH=${PATH}:${MAVEN_HOME}/bin  
  

