FROM java:8-jdk-alpine  
  
ENV SBT_VERSION 0.13.15  
ENV PATH ${PATH}:/usr/local/sbt/bin  
  
RUN apk add --no-cache --update bash git protobuf make mysql-client && \  
wget -q -O - "http://dl.bintray.com/sbt/native-
packages/sbt/${SBT_VERSION}/sbt-${SBT_VERSION}.tgz" | \  
gunzip | tar -x -C /usr/local && \  
echo -ne "- with sbt ${SBT_VERSION}\n" >> /root/.built  
  
WORKDIR /app  

