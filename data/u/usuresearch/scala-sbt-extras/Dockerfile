FROM openjdk:8-jdk-slim  
  
MAINTAINER USU Software AG  
  
  
RUN \  
apt-get update && \  
apt-get install -yq curl git-core && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
# sbt 1.0.3 / latest Scala 2.12  
RUN \  
curl -s https://raw.githubusercontent.com/paulp/sbt-extras/master/sbt >
/usr/local/bin/sbt && chmod 0755 /usr/local/bin/sbt && \  
sbt about -sbt-create -sbt-version 1.0.3 -212  
  
WORKDIR /root  

