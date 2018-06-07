FROM openjdk:8  
LABEL maintainer="Marco Antonio Martins Júnior (somatorio@gmail.com)"  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends x11-xserver-utils && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
wget http://s3.amazonaws.com/Minecraft.Download/launcher/Minecraft.jar -O
/root/Minecraft.jar  
  
CMD [ "java", "-jar", "/root/Minecraft.jar" ]  

