FROM openjdk:8-jre-alpine  
  
ARG CHECKSTYLE_VERSION=8.2  
ADD
http://downloads.sourceforge.net/project/checkstyle/checkstyle/${CHECKSTYLE_VERSION}/checkstyle-${CHECKSTYLE_VERSION}-all.jar
/checkstyle.jar  
ADD
https://raw.githubusercontent.com/checkstyle/checkstyle/master/src/main/resources/google_checks.xml
/google_checks.xml  
ADD
https://raw.githubusercontent.com/checkstyle/checkstyle/master/src/main/resources/sun_checks.xml
/sun_checks.xml  
  
ENTRYPOINT ["java", "-jar", "/checkstyle.jar"]  

