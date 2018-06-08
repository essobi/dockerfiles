FROM openjdk  
  
MAINTAINER rsears  
  
COPY /pom.xml pom.xml  
COPY /src/main/java src/main/java  
ADD /src/main/resources/processing/sample_product_data.tsv
sample_product_data.tsv  
ADD /release/processing-1.0-SNAPSHOT.jar processing.jar  
COPY /conf/processing.yml conf/processing.yml  
  
EXPOSE 8080-8081  
ENTRYPOINT ["java", "-Xmx2G", "-jar", "processing.jar"]  
CMD ["server", "conf/processing.yml"]

