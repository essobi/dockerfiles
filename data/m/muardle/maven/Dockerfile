FROM openjdk:8-alpine  
  
ENV MAVEN_VERSION="3.5.3"  
RUN apk add --no-cache \  
curl  
  
RUN curl -O --location
https://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.zip && \  
mkdir /opt && \  
unzip -q apache-maven-${MAVEN_VERSION}-bin.zip -d /opt && \  
ln -s /opt/apache-maven-${MAVEN_VERSION} /opt/maven && \  
rm -f apache-maven-${MAVEN_VERSION}-bin.zip  
  
ENV PATH $PATH:/opt/maven/bin  
  
WORKDIR /etc/maven  
  
ENTRYPOINT ["mvn"]  

