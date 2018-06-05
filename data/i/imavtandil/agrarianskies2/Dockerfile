FROM debian:wheezy  
  
RUN apt-get -y update  
RUN apt-get -y install openjdk-7-jre-headless wget unzip  
RUN mkdir /server  
RUN wget -q https://minecraft.curseforge.com/projects/agrarian-
skies-2/files/2261980/download -O /server/pack.zip  
  
RUN cd /server && unzip pack.zip && rm pack.zip  
CMD java -jar ./minecraft_server.1.7.10.jar  

