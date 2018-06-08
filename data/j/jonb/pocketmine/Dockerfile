FROM ubuntu:trusty  
MAINTAINER Jon Bjornn <jonbjornn@gmail.com>  
  
RUN apt-get -y install python3-yaml  
  
RUN mkdir /pocketmine  
RUN cd /pocketmine && wget -q -O - http://get.pocketmine.net/ | bash -s - -r
-v development  
  
VOLUME /pocketmine  
WORKDIR /pocketmine  
  
EXPOSE 19132  
CMD ["./start.sh", "--no-wizard", "--enable-rcon=on"]  

