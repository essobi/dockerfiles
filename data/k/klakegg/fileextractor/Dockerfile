FROM maven:3.3.9-jdk-8 AS mvn  
  
ADD . $MAVEN_HOME  
  
RUN cd $MAVEN_HOME \  
&& mvn -B clean package \  
&& mv $(ls $MAVEN_HOME/target/*.jar | grep jar-with-dependencies | head -1)
/fileextractor.jar  
  
FROM java:8-jre-alpine  
  
COPY \--from=mvn /fileextractor.jar /fileextractor.jar  
  
VOLUME /src /target  
  
WORKDIR /src  
ENTRYPOINT ["java", "-jar", "/fileextractor.jar"]

