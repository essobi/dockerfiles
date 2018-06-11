FROM maven:3-jdk-8  
MAINTAINER Martin Humpolec <kbc@htns.cz>  
  
ENV APP_VERSION 1.1.0  
WORKDIR /home  
RUN git clone https://mhumpolec@bitbucket.org/mhumpolec/kbc-wave-writer.git ./  
RUN mvn compile  
  
ENTRYPOINT mvn -q exec:java -Dexec.args=/data

