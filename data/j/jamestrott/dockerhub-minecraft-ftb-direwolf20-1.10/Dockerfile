# This is based on itzg/minecraft-server  
# forked from gunsmithy/ftb-direwolf20-1.10  
FROM openjdk:8-jre  
  
MAINTAINER James Trott  
  
RUN apt-get update && apt-get install -y wget unzip  
  
COPY entry.sh /srv/entry.sh  
  
WORKDIR /srv  
  
RUN wget -c https://www.feed-the-beast.com/projects/ftb-presents-
direwolf20-1-10/files/2435268/download -O server.zip && \  
unzip server.zip && \  
rm server.zip && \  
echo "eula=TRUE" > eula.txt && \  
/bin/bash FTBInstall.sh && \  
chmod +x ServerStart.sh  
  
EXPOSE 25565  
CMD ["/bin/bash","entry.sh"]  

