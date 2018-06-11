FROM maven:3.5-jdk-8-alpine as build  
  
VOLUME /tmp  
  
WORKDIR /code  
  
# Prepare by downloading dependencies  
ADD pom.xml /code/pom.xml  
#RUN ["mvn", "dependency:resolve"]  
#RUN ["mvn", "verify"]  
# Adding source, compile and package into a fat jar  
ADD src /code/src  
RUN ["mvn", "clean", "install"]  
  
RUN ["ls", "/code/target"]  
RUN ["pwd"]  
RUN ["ls", "-ltrh", "/code/target/RestFrameWorkUtility-1.0.0.war"]  
  
From tomcat:8-jre8  
MAINTAINER "siddu.v444@gmail.com"  
WORKDIR /code  
  
EXPOSE 8080  
# Copy to images tomcat path  
#RUN ["ls","/code/target"]  
#ADD code/target/RestFrameWorkUtility-1.0.0.war /usr/local/tomcat/webapps/  
COPY \--from=build code/target/RestFrameWorkUtility-1.0.0.war
/usr/local/tomcat/webapps/  
  
RUN ["ls", "/usr/local/tomcat/webapps/"]  
#ADD target/SpringKube.jar SpringKube.jar  
#ENTRYPOINT ["java","-jar","SpringKube.jar"]  
CMD ["catalina.sh", "run"]  
#ENTRYPOINT [ "java", "-jar", "/code/target/myspringboot.jar" ]  
##FROM tomcat  
#MAINTAINER ardy.dedase@gmail.com  
#ADD /usr/src/movieplex7/target/movieplex7-1.0-SNAPSHOT.war
/usr/local/tomcat/webapps/  
#COPY --from=app /usr/spring4-form-handle-
example/target/movieplex7-1.0-SNAPSHOT.war .  
#CMD ["catalina.sh", "run"]  

