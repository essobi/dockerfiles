FROM ubuntu:14.04  
MAINTAINER xforty technologies  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -qqy upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qqy install wget perl build-
essential gcc-multilib  
  
RUN adduser --gecos 'PocketMine-MP' \--disabled-password --home /pocketmine
pocketmine  
  
WORKDIR /pocketmine  
RUN chown -R pocketmine:pocketmine /pocketmine  
  
USER pocketmine  
  
ENV GNUPGHOME /pocketmine  
  
RUN gpg --keyserver pgp.mit.edu --recv-key 2280B75B  
RUN wget -q -O - http://cdn.pocketmine.net/installer.sh | bash -s - -v beta  
  
EXPOSE 19132  
EXPOSE 19132/udp  
  
CMD ["./start.sh","--data","/data"]  
  

