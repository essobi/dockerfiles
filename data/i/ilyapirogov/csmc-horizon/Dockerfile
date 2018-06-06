FROM java:openjdk-8-jdk  
MAINTAINER Ilya Pirogov <ilja.pirogov@gmail.com>  
  
WORKDIR /var/app/horizon  
  
ADD ./setup-env.sh /  
  
ENV MINECRAFT_VERSION 1.7.10  
ENV FORGE_VERSION 10.13.4.1558  
# see sha1 on
http://files.minecraftforge.net/maven/net/minecraftforge/forge/index_1.7.10.html  
ENV FORGE_INSTALLER_SHA1 afcf4b3392b6d632acb728b78b1a6321ee59ac61  
  
RUN /setup-env.sh  
  
ENV JVM_XMS 8g  
ENV JVM_XMX 16g  
ENV JVM_ADDITIONAL -XX:+UseStringCache -XX:+OptimizeStringConcat
-XX:+AggressiveOpts -XX:+UseParNewGC -XX:+UseConcMarkSweepGC  
ENV JMX_HOSTNAME ""  
ENV JMX_PORT 3333  
ENV RCON_PASSWORD nopass  
  
ENV TWITCH_CHANNEL mjramon  
ENV TWITCH_TOKEN ""  
ADD ./mcrcon /usr/local/bin/  
ADD ./entrypoint.sh /  
  
VOLUME /var/app/horizon/world  
VOLUME /var/app/horizon/config  
  
EXPOSE 3333  
EXPOSE 3334  
EXPOSE 25565  
EXPOSE 25575  
ADD ./horizon/*.json /var/app/horizon/original/  
ADD ./horizon/ForgeEssentials /var/app/horizon/original/ForgeEssentials  
ADD ./horizon/server.properties /var/app/horizon/  
ADD ./horizon/config /var/app/horizon/config  
ADD ./horizon/mods /var/app/horizon/mods  
ADD ./horizon/scripts /var/app/horizon/scripts  
ADD ./horizon/local /var/app/horizon/local  
ADD ./horizon/server-icon.png /var/app/horizon/  
  
ENTRYPOINT /entrypoint.sh  

