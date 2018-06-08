FROM debian:jessie  
  
RUN apt-get update && apt-get install -y curl python3-yaml perl gcc g++ make
automake libtool autoconf m4  
  
RUN mkdir /pocketmine  
RUN cd /pocketmine && curl -sL
https://raw.githubusercontent.com/PocketMine/php-build-
scripts/master/installer.sh | bash -s - -v development -r  
  
WORKDIR /pocketmine  
  
EXPOSE 19132  
CMD ["./start.sh", "--no-wizard", "--enable-rcon=on"]  
  
VOLUME /pocketmine  

