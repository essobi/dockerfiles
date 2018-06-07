# Sponge Powered Minecraft Modded Server  
FROM java:8  
MAINTAINER John Starich <johnstarich@johnstarich.com>  
  
# Set default environment variables  
ENV MINECRAFT_PORT 25565  
ENV SPONGE_VERSION latest  
  
# Expose default port (any other port require manual publishing)  
EXPOSE 25565  
EXPOSE 25565/udp  
  
# Add persistent storage for the sponge server  
VOLUME ["/sponge"]  
  
WORKDIR /sponge  
  
RUN DEBIAN_FRONTEND=noninterative \  
apt-get update && \  
apt-get install -y jq && \  
apt-get clean autoclean && \  
rm -rf /var/lib/apt/* /var/lib/cache/* /var/lib/log/*  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["-Xms256M"]  
COPY ./entrypoint.sh /entrypoint.sh  
COPY ./bin /usr/bin  

