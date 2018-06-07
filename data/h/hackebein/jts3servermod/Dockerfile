FROM openjdk:8-jre-alpine  
  
ARG JTS3_SERVER_MOD_VERSION=6.4.4  
ARG JTS3_SERVER_MOD_FOLDER=JTS3ServerMod_HostingEdition  
ARG
JTS3_SERVER_MOD_FILE=${JTS3_SERVER_MOD_FOLDER}_${JTS3_SERVER_MOD_VERSION}.zip  
  
RUN apk update && apk add \  
wget \  
paxctl \  
&& paxctl -cm `which java` \  
&& wget https://www.stefan1200.de/downloads/${JTS3_SERVER_MOD_FILE} -O
/tmp/${JTS3_SERVER_MOD_FILE} \  
&& mkdir -p /opt/jts3servermod \  
&& unzip -d /tmp /tmp/${JTS3_SERVER_MOD_FILE} \  
&& mv /tmp/${JTS3_SERVER_MOD_FOLDER}/plugins /opt/jts3servermod/ \  
&& mv /tmp/${JTS3_SERVER_MOD_FOLDER}/JTS3ServerMod.jar /opt/jts3servermod/ \  
&& rm -rf \  
/tmp/${JTS3_SERVER_MOD_FOLDER} \  
/tmp/${JTS3_SERVER_MOD_FILE} \  
&& apk del \  
wget  
  
COPY config /opt/jts3servermod/config  
  
VOLUME \  
/opt/jts3servermod/config \  
/opt/jts3servermod/plugins \  
/opt/jts3servermod/log  
  
WORKDIR /opt/jts3servermod  
  
ENTRYPOINT ["java", "-XX:+UnlockExperimentalVMOptions",
"-XX:+UseCGroupMemoryLimitForHeap", "-jar", "JTS3ServerMod.jar", "-log",
"log/JTS3ServerMod_InstanceManager.log"]  

