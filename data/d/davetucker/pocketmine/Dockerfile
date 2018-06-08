FROM debian:jessie  
MAINTAINER Dave Tucker <dave@dtucker.co.uk>  
  
RUN apt-get -qq update && apt-get -qq -y install curl  
RUN mkdir -p pocketmine  
WORKDIR pocketmine  
RUN curl -sL https://raw.githubusercontent.com/PocketMine/php-build-
scripts/master/installer.sh | bash -s - -r  
CMD ["./start.sh"]  
  
VOLUME /pocketmine/server.properties  
VOLUME /pocketmine/pocketmine.yml  
VOLUME /pocketmine/worlds/world  
EXPOSE 19132/udp  

