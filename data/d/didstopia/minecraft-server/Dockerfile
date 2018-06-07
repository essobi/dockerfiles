FROM didstopia/base:alpine-3.5  
LABEL maintainer="Didstopia <support@didstopia.com>"  
  
# System variables for use with installation  
ENV _JAVA_OPTIONS "-XX:+UseG1GC -Djava.security.egd=file:/dev/urandom"  
ENV PATH "${PATH}:/opt/jdk/bin"  
ENV LANG "C.UTF-8"  
# Minecraft server specific environment variables  
ENV MINECRAFT_SERVER_VERSION "1.12.2"  
ENV MINECRAFT_SERVER_MEMORY_MIN "1G"  
ENV MINECRAFT_SERVER_MEMORY_MAX "1G"  
ENV MINECRAFT_SERVER_AGREE_EULA "true"  
ENV MINECRAFT_SERVER_ARGUMENTS "nogui"  
# Install dependencies  
RUN apk --no-cache add \  
openjdk8-jre \  
wget \  
ca-certificates \  
bash  
  
# Install the latest Minecraft server  
RUN wget --no-check-certificate \  
"https://s3.amazonaws.com/Minecraft.Download/versions/${MINECRAFT_SERVER_VERSION}/minecraft_server.${MINECRAFT_SERVER_VERSION}.jar"
\  
-O "/minecraft_server.jar"  
RUN chmod +x /minecraft_server.jar  
  
# Copy the startup scripts (which also handles automatic updates)  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
# Run as the "docker" user by default  
ENV PGID 1000  
ENV PUID 1000  
# Expose the default server port  
EXPOSE 25565  
# Set the startup command  
CMD ["/bin/bash", "/start.sh"]  

