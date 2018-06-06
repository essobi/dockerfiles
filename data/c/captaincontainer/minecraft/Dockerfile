FROM alpine:latest  
  
MAINTAINER ajohnson@petrichor.io  
  
ENV VERSION=1.10.2  
ENV EULA=true  
ENV MAXMEM=512M  
ENV MINMEM=512M  
  
RUN mkdir /minecraft  
RUN apk --update add wget ca-certificates openjdk8-jre  
  
RUN wget -O /minecraft/minecraft.jar
https://s3.amazonaws.com/Minecraft.Download/versions/$VERSION/minecraft_server.$VERSION.jar  
RUN echo "eula=$EULA" >> /minecraft/eula.txt  
  
VOLUME /minecraft  
WORKDIR /minecraft  
EXPOSE 25565  
CMD /usr/bin/java -Xmx${MAXMEM} -Xms${MINMEM} -jar minecraft.jar nogui  

