FROM maven:3.3.9-jdk-8-onbuild  
  
ENV PORT 3000  
  
  
CMD ["java", "-javaagent:newrelic/newrelic.jar", "-jar", "target/rest-
api.jar"]

