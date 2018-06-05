# Minecraftly Server Dockerfile  
# Use the offical Java Docker image  
FROM java:8  
MAINTAINER Viet Nguyen <http://vi.et>  
  
# Use APT (Advanced Packaging Tool) built in the Linux distro to download
Java, a dependency  
# to run Minecraft.  
RUN apt-get -y update  
RUN apt-get -y dist-upgrade  
RUN apt-get -y install wget  
  
#RUN useradd -M -s /bin/false --uid 1000 minecraftly \  
# && mkdir /data \  
# && mkdir /plugins \  
# && chown minecraftly:minecraftly /data /plugins  
# Download Minecraft Server components  
RUN wget -q
https://s3.amazonaws.com/Minecraft.Download/versions/1.10.2/minecraft_server.1.10.2.jar  
  
# Sets working directory for the CMD instruction (also works for RUN,
ENTRYPOINT commands)  
# Create mount point, and mark it as holding externally mounted volume  
WORKDIR /data  
VOLUME /data  
  
# Define commonly used JAVA_HOME variable  
#ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# Define default command.  
#CMD ["bash"]  
# Expose the container's network port: 25565 during runtime.  
EXPOSE 25565  
#Automatically accept Minecraft EULA, and start Minecraft server  
CMD echo eula=true > /data/eula.txt && java -jar /minecraft_server.1.10.2.jar

