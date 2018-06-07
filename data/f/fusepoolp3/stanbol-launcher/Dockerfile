FROM maven:3.2-jdk-8  
MAINTAINER Reto Gmür <me@farewellutopia.com>  
  
EXPOSE 8080  
#Prepare  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Build  
COPY ./ /usr/src/app  
RUN mvn install -DfinalName=stanbol-p3  
  
ENTRYPOINT ["java"]  
# The default launcher with all the NLP models needs about 8GByte Heap  
CMD ["-jar", "-Xmx8g", "launcher/default/target/stanbol-p3.jar"]  

