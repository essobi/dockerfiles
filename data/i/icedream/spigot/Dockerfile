FROM java:8-alpine  
  
ARG MINECRAFT_VERSION=1.11.2  
ARG SPIGOT_BUILD=1235  
WORKDIR /usr/src/spigot  
ADD
https://hub.spigotmc.org/jenkins/job/BuildTools/59/artifact/target/BuildTools.jar
/usr/src/spigot/BuildTools.jar  
RUN \  
apk add --no-cache --virtual .temp-deps \  
git \  
&& java -jar BuildTools.jar --rev "${SPIGOT_BUILD}" \  
&& mv spigot*.jar /srv/spigot.jar \  
&& chmod 444 /srv/spigot.jar  
  
ADD start.sh /usr/local/bin/spigot  
RUN chmod +x /usr/local/bin/spigot  
  
ENV JAVA_ARGS "-Xmx1G"  
ENV SPIGOT_ARGS ""  
ENV PAPER_ARGS ""  
WORKDIR /data  
VOLUME "/data"  
  
CMD ["spigot"]  

