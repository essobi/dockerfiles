FROM debian:unstable  
  
  
LABEL maintainer "doconnell@cursived.com"  
  
RUN apt-get update && apt-get upgrade --yes && apt-get install --yes \  
openjdk-8-jre-headless \  
openssl \  
imagemagick \  
lsof \  
gosu \  
bash \  
curl \  
git \  
jq \  
mysql-client \  
sqlite \  
htop \  
python python-dev  
  
RUN adduser --shell /bin/false \--uid=1000 --home /home/minecraft minecraft \  
&& mkdir /data \  
&& mkdir /config \  
&& mkdir /mods \  
&& mkdir /plugins \  
&& chown minecraft:minecraft /data /config /mods /plugins /home/minecraft  
  
EXPOSE 25565 25575  
ADD
https://github.com/itzg/restify/releases/download/1.0.4/restify_linux_amd64
/usr/local/bin/restify  
ADD https://github.com/itzg/rcon-cli/releases/download/1.3/rcon-
cli_linux_amd64 /usr/local/bin/rcon-cli  
COPY start.sh /start  
COPY start-minecraft.sh /start-minecraft  
COPY mcadmin.jq /usr/share  
RUN chmod +x /usr/local/bin/*  
  
VOLUME ["/data","/mods","/config","/plugins","/home/minecraft"]  
COPY server.properties /tmp/server.properties  
WORKDIR /data  
  
CMD [ "/start", "--noconsole" ]  
  
ENV UID=1000 GID=1000 \  
MOTD="A Minecraft Server Powered by Docker" \  
JVM_XX_OPTS="-XX:+UseG1GC" MEMORY="1G" \  
TYPE=VANILLA VERSION=LATEST FORGEVERSION=RECOMMENDED LEVEL=world PVP=true
DIFFICULTY=easy \  
ENABLE_RCON=true RCON_PORT=25575 RCON_PASSWORD=minecraft \  
LEVEL_TYPE=DEFAULT GENERATOR_SETTINGS= WORLD= MODPACK= ONLINE_MODE=TRUE
CONSOLE=true  

