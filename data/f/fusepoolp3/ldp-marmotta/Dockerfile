FROM maven:3.2-jdk-8  
MAINTAINER Reto Gmür <me@farewellutopia.com>  
  
EXPOSE 8080  
#Prepare  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Build  
COPY ./ /usr/src/app  
RUN mvn install -DfinalName=marmotta  
  
ENV MARMOTTA_HOME /usr/src/app  
  
RUN echo "security.enabled = false" > system-config.properties  
  
ENTRYPOINT ["java"]  
CMD ["-jar", "webapp/target/marmotta.jar"]  

