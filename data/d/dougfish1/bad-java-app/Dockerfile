FROM maven:3.5-jdk-8-alpine as build  
COPY pom.xml /pom.xml  
COPY src /src  
RUN mkdir /target  
RUN mkdir /classes  
#RUN bash -c 'mvn package'  
#RUN mvn dependency:copy-dependencies  
RUN mvn package  
  
FROM tomcat:7-jre8-alpine  
RUN apk --no-cache add curl  
COPY \--from=build /target/bad-java-test-app-1.0.0.war
/usr/local/tomcat/webapps/bad-java-test-app.war  
CMD ["catalina.sh", "run"]  

