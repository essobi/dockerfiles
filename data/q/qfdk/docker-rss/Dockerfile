FROM java:7  
ENV INSPECTIT_CONFIG_HOME /agent-config  
  
RUN apt-get update && apt-get install -y git wget libgradle-core-java  
  
# forked repository  
RUN git clone https://github.com/qfdk/recipes-rss-compile recipes-rss  
  
#download the agent  
WORKDIR /  
RUN wget
https://github.com/inspectIT/inspectIT/releases/download/1.6.6.76/inspectit-
agent-sun1.5.zip  
RUN unzip inspectit-agent-sun*.zip  
  
#build the netflix rss reader  
WORKDIR /recipes-rss  
ENV APP_ENV=dev  
RUN ./gradlew clean build  
  
EXPOSE 9090 9092  
#start jar  
WORKDIR /recipes-rss  
CMD ["java","-jar","rss-edge/build/libs/rss-edge-0.1.0-SNAPSHOT.jar"]

