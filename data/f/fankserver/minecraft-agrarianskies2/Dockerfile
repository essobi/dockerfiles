FROM openjdk:7-jre-alpine  
  
LABEL maintainer "Florian Kinder <florian.kinder@fankserver.com>"  
  
RUN apk add --no-cache wget ca-certificates && \  
mkdir /server && \  
wget https://minecraft.curseforge.com/projects/agrarian-
skies-2/files/2261980/download -O /tmp/AS2-1.1.14-Server.zip && \  
unzip /tmp/AS2-1.1.14-Server.zip -d /server && \  
rm /tmp/AS2-1.1.14-Server.zip && \  
echo "eula=true" > /server/eula.txt && \  
mv /server/world /server/world_org && \  
mv /server/config /server/config_org  
  
COPY start.sh /start.sh  
WORKDIR /server  
  
EXPOSE 25565  
CMD ["/start.sh"]  

