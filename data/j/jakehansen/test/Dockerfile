FROM debian:wheezy  
  
# Use APT (Advanced Packaging Tool) built in the Linux distro to download
Java, a dependency  
# to run Minecraft.  
RUN \  
apt-get -y update && \  
apt-get -y install openjdk-7-jre-headless wget && \  
apt-get -y install zip  
  
# Download Minecraft Server components  
RUN \  
wget -q
http://ftb.cursecdn.com/FTB2/modpacks/FTBInfinity/1_10_1/FTBInfinityServer.zip
&& \  
unzip FTBInfinityServer.zip && \  
wget -O minecraft_server.1.7.10.jar
https://s3.amazonaws.com/Minecraft.Download/versions/1.7.10/minecraft_server.1.7.10.jar
&& \  
wget -O libraries/net/minecraft/launchwrapper/1.11/launchwrapper-1.11.jar
https://libraries.minecraft.net/net/minecraft/launchwrapper/1.11/launchwrapper-1.11.jar  
  
RUN \  
chmod +x FTBServer-1.7.10-1448.jar && \  
mkdir data  
  
# Sets working directory for the CMD instruction (also works for RUN,
ENTRYPOINT commands)  
# Create mount point, and mark it as holding externally mounted volume  
WORKDIR /data  
VOLUME /data  
  
# Expose the container's network port: 25565 during runtime.  
EXPOSE 25565  
#Automatically accept Minecraft EULA, and start Minecraft server  
CMD echo eula=true > /data/eula.txt && java -server -Xms512m -Xmx2048M
-XX:PermSize=256m -d64 -XX:+UseParNewGC -XX:+CMSIncrementalPacing
-XX:+CMSClassUnloadingEnabled -XX:ParallelGCThreads=2 -XX:MinHeapFreeRatio=5
-XX:MaxHeapFreeRatio=10 -jar FTBServer-1.7.10-1448.jar nogui

