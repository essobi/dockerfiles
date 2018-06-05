FROM tomcat:8.5.0-jre8  
  
ENV calculator_service_version 3.3  
RUN wget https://jitpack.io/com/github/dev-tool-index/calculator-
service/${calculator_service_version}/calculator-
service-${calculator_service_version}.war -O
/usr/local/tomcat/webapps/calculator-service.war  
  
CMD ["catalina.sh", "run"]  

