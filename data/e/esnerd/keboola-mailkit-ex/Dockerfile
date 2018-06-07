# instead of maven:3.5.0-jdk-8-alpine, contained old java version  
FROM maven:3.5.2-jdk-8-slim  
  
  
MAINTAINER David Esner <esnerda@gmail.com>  
  
ENV APP_VERSION 1.1.0  
# install git  
RUN apt-get update -y  
RUN apt-get install -y git-core  
  
# set switch that enables correct JVM memory allocation in containers  
ENV JAVA_OPTS "-XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap"  
ENV MAVEN_OPTS "-XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap"  
WORKDIR /home  
RUN git clone https://github.com/davidesner/keboola-mailkit-ex.git ./  
RUN mvn -q install  
  
ENTRYPOINT java -jar target/esnerda.keboola.ex.mailkit-1.1.0-jar-with-
dependencies.jar /data

