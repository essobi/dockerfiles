FROM maven:3-jdk-8  
MAINTAINER Warner Godfrey <w@godfrey.io>  
LABEL Description="Tools to work with Amazon API Gateway and Swagger"  
  
ADD aws-api-import.sh pom.xml /var/app/  
ADD src /var/app/src/  
ADD tst /var/app/tst/  
  
WORKDIR /var/app  
  
RUN mvn assembly:assembly  
RUN cp build/maven/aws-apigateway-swagger-importer-1.0.0-jar-with-
dependencies.jar .  
RUN mvn clean  
RUN mkdir -p build/maven  
RUN mv aws-apigateway-swagger-importer-1.0.0-jar-with-dependencies.jar
build/maven  
RUN rm -rf pom.xml src tst  
RUN rm -rf ~/.m2  
  
ENTRYPOINT ["/var/app/aws-api-import.sh"]  
CMD ["--help"]  

