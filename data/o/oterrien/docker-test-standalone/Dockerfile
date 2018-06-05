FROM openjdk:8u111-jdk  
  
RUN MAVEN_VERSION=3.3.3 \  
&& cd /usr/share \  
&& wget
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz -O - | tar xzf - \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
WORKDIR /code  
  
ADD pom.xml /code/pom.xml  
ADD src/main /code/src/main  
RUN ["mvn", "package"]  
  
EXPOSE 8080  
CMD ["java", "-jar", "target/docker-test-standalone.jar"]

