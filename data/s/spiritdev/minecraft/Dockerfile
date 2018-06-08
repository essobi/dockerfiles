FROM spiritdev/openjdk-7  
MAINTAINER Jean Bordat <bordat.jean@gmail.com>  
  
ENV APT_GET_UPDATE 2015-03-28  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libmozjs-24-bin sudo
imagemagick && apt-get clean  
RUN update-alternatives --install /usr/bin/js js /usr/bin/js24 100  
  
RUN wget -O /usr/bin/jsawk https://github.com/micha/jsawk/raw/master/jsawk  
RUN chmod +x /usr/bin/jsawk  
RUN useradd -M -s /bin/false \--uid 1000 minecraft \  
&& mkdir /data \  
&& chown minecraft:minecraft /data  
  
EXPOSE 25565  
COPY start.sh /start  
COPY start-minecraft.sh /start-minecraft  
  
VOLUME ["/data"]  
COPY server.properties /tmp/server.properties  
WORKDIR /data  
  
RUN chmod 755 /start  
CMD [ "/start" ]  
  
# Special marker ENV used by MCCY management tool  
ENV MC_IMAGE YES  
  
ENV UID 1000  
ENV MOTD Minecraft Server -_- Powered by Docker and Spirit-Dev.  
ENV JVM_OPTS -Xmx1024M -Xms1024M  
ENV TYPE=VANILLA VERSION=LATEST LEVEL=world PVP=true  
#ENV TYPE VANILLA  
#ENV VERSION LATEST  
#ENV LEVEL world  
#ENV PVP true  

