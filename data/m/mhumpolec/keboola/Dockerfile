FROM maven:3.5.2-jdk-8-slim  
MAINTAINER Martin Humpolec <kbc@htns.cz>  
  
ENV APP_VERSION 1.1.0  
# install git  
RUN apt-get update -y  
RUN apt-get install -y git-core  
  
WORKDIR /home  
RUN git clone -b 1.0.7 https://mhumpolec@bitbucket.org/mhumpolec/keboola.git
./  
RUN mvn compile  
  
ENTRYPOINT mvn -q exec:java -Dexec.args=/data  

