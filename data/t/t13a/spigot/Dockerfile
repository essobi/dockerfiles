FROM debian:stretch AS builder  
  
ARG SPIGOT_VERSION=latest  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y install curl git openjdk-8-jre-headless && \  
mkdir /spigot && \  
cd /spigot && \  
curl -Lo BuildTools.jar
https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
&& \  
java -jar BuildTools.jar --rev "${SPIGOT_VERSION}"  
  
FROM anapsix/alpine-java  
  
RUN apk add --no-cache --update bash darkhttpd s6  
  
COPY \--from=builder /spigot/spigot-*.jar /spigot/spigot.jar  
  
ADD /rootfs /  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
  
CMD [ "s6-svscan", "-s", "/s6" ]  

