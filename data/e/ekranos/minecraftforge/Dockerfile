FROM ekranos/debianjava  
  
MAINTAINER Marvin Lee Fimmel <kontakt@ekranos.me>  
  
RUN mkdir -p /shared/server && cd /shared && echo "eula=true" >> eula.txt && \  
wget
http://files.minecraftforge.net/maven/net/minecraftforge/forge/1.8-11.14.4.1577/forge-1.8-11.14.4.1577-installer.jar
-O forgeinstaller.jar && \  
java -jar forgeinstaller.jar -installServer  
  
ADD ./scripts/start /shared/start  
  
WORKDIR /shared/server  
  
VOLUME /shared/server  
  
EXPOSE 25565  
CMD ["/shared/start"]  

