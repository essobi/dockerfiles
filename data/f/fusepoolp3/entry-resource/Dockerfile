FROM maven:3.2-jdk-8  
MAINTAINER Reto Gmür <me@farewellutopia.com>  
  
#Prepare  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Build  
COPY ./ /usr/src/app  
  
RUN mvn install -DfinalName=p3-entry-launcher  
  
ENTRYPOINT ["java"]  
CMD ["-jar", "launcher/target/p3-entry-launcher.jar"]  

