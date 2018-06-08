FROM ubuntu:14.04  
LABEL REVISION unknown  
RUN apt-get update && apt-get install -y wget curl \  
openjdk-7-jdk  
RUN apt-get clean  
ENV APP_PORT 8080  
EXPOSE 80 8080  
WORKDIR /home/root/src  
  
COPY src /home/root/src  
RUN javac /home/root/src/HelloWorld.java  
ENTRYPOINT ["java", "HelloWorld"]  

