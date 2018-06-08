# escape=`  
FROM openjdk:8-jre  
  
ARG BUILDNODE=unspecified  
ARG SOURCE_COMMIT=unspecified  
  
LABEL maintainer="Laclede's LAN <contact @lacledeslan.com>" `  
com.lacledeslan.build-node=$BUILDNODE `  
org.label-schema.schema-version="1.0" `  
org.label-schema.url="https://github.com/LacledesLAN/README.1ST" `  
org.label-schema.vcs-ref=$SOURCE_COMMIT `  
org.label-schema.vendor="Laclede's LAN" `  
org.label-schema.description="Minecraft (Java Client) Dedicated Server in
Docker" `  
org.label-schema.vcs-url="https://github.com/LacledesLAN/gamesvr-minecraft"  
RUN apt-get update && apt-get install -y `  
procps screen &&`  
apt-get clean &&`  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*;  
  
# Set up Enviornment  
RUN useradd --home /app --gid root --system Minecraft &&`  
mkdir --parents /app &&`  
chown Minecraft:root -R /app;  
  
COPY eula.txt /app/eula.txt  
  
COPY ./ll-tests /app/ll-tests  
  
RUN chmod +rx /app/ll-tests/*.sh &&`  
chmod +rwx -R /app &&`  
chown Minecraft:root -R /app/ll-tests;  
  
USER Minecraft  
  
RUN curl -sSL
"https://s3.amazonaws.com/Minecraft.Download/versions/1.12.2/minecraft_server.1.12.2.jar"
-o /app/minecraft-server.jar &&`  
echo "886945bfb2b978778c3a0288fd7fab09d315b25f /app/minecraft-server.jar" |
sha1sum -c - && `  
chmod +rwx /app/*.jar;  
  
WORKDIR /app  
  
ONBUILD USER root  

