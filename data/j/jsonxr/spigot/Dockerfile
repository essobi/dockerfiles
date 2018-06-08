FROM java:8  
MAINTAINER jsonxr <jsonxr@gmail.com>  
  
ENV SPIGOT_VERSION=1.11  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wget git && \  
apt-get clean all && \  
useradd -s /bin/bash -d /minecraft -m minecraft && \  
mkdir /minecraft-build && \  
cd /minecraft-build && \  
wget
https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
&& \  
HOME=/minecraft-build java -jar BuildTools.jar --rev 1.11  
  
# Copy start script and defaults  
COPY /src/ /  
  
# expose minecraft port  
EXPOSE 25565  
WORKDIR /minecraft  
VOLUME /minecraft  
  
#set default command  
CMD ["java", "-Xms1024M", "-Xmx4096M", "-jar", "spigot.jar"]  

