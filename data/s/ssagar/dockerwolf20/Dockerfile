# Container info  
FROM ubuntu:vivid  
MAINTAINER Sunny Sagar trexinabluecape@gmail.com  
ENV MC_VER 1.7.10  
ENV DW20_VER 1_8_0  
ENV MIN_MEM 2048  
ENV MAX_MEM 4096  
# Install prerequisites  
RUN apt-get -qq update &&\  
apt-get -yqq install openjdk-8-jdk java-common curl unzip > /dev/null 2>&1 &&\  
apt-get -qq clean  
  
# Set up volumes and directories  
VOLUME /opt/minecraft-data  
  
# Grab the server and store it in /opt  
RUN curl -o /opt/server.zip\  
http://ftb.cursecdn.com/FTB2/modpacks/direwolf20_17/$DW20_VER/direwolf20_17-server.zip  
  
# Add start script  
ADD initialize.sh /opt/  
RUN chmod +x /opt/initialize.sh  
  
# Expose port  
EXPOSE 25565:25565  
# Default command  
ENTRYPOINT ["/opt/initialize.sh"]  
  

