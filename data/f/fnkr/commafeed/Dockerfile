FROM debian:wheezy  
  
RUN apt-get update  
RUN apt-get install -y git  
  
RUN mkdir /commafeed  
RUN mkdir /config  
RUN mkdir /data  
WORKDIR /commafeed  
  
RUN apt-get install -y build-essential  
RUN apt-get install -y openjdk-7-jdk  
RUN apt-get install -y maven  
  
ENV COMMAFEED_GIT https://github.com/Athou/commafeed.git  
ENV COMMAFEED_VERSION 2.1.0  
RUN git clone $COMMAFEED_GIT .  
RUN git checkout $COMMAFEED_VERSION  
  
RUN mvn clean package  
  
RUN cp /commafeed/config.dev.yml /config/config.yml  
VOLUME /config  
VOLUME /data  
  
WORKDIR /data  
ENTRYPOINT java -jar /commafeed/target/commafeed.jar server /config/config.yml  

