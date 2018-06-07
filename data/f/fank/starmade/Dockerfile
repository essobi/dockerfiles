FROM openjdk:jre  
  
RUN mkdir -p /starmade &&\  
cd /tmp &&\  
wget -q http://files.star-made.org/StarMade-Starter.jar &&\  
ln -s /starmade StarMade &&\  
java -jar ./StarMade-Starter.jar -nogui &&\  
rm StarMade StarMade-Starter.jar  
  
COPY server.cfg /starmade/server-example.cfg  
  
VOLUME /starmade/server-database/  
VOLUME /starmade/config/  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
WORKDIR /starmade  
  
EXPOSE 4242  

