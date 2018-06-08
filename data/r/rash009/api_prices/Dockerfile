FROM java  
MAINTAINER Sathish Arulmani <s.arulmani@exchange-data.com>  
  
ENTRYPOINT ["java", "-jar", "myservice.jar"]  
  
ARG JAR_FILE  
ADD target/${JAR_FILE} myservice.jar

