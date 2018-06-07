FROM maven:3.5-jdk-8-alpine as build  
  
COPY ./pom.xml /workspace/pom.xml  
COPY ./src /workspace/src  
COPY ./.git /workspace/.git  
COPY tools /workspace/tools  
WORKDIR /workspace  
RUN mvn install  
  
#ENTRYPOINT ["/bin/bash"]  
#  
FROM openjdk:8-jre-alpine  
  
RUN apk add --no-cache bash  
  
COPY \--from=build /workspace/target/releases/*.zip /workspace/  
  
WORKDIR /workspace  
  
RUN unzip /workspace/*.zip  

