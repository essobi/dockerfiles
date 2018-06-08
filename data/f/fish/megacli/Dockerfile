FROM ubuntu  
MAINTAINER Johannes 'fish' Ziemke <fish@docker.com> @discordianfish  
  
RUN apt-get -y -q update && apt-get -y -q install curl  
RUN curl http://hwraid.le-vert.net/debian/hwraid.le-vert.net.gpg.key | apt-key
add -  
RUN echo deb http://hwraid.le-vert.net/ubuntu precise main >>
/etc/apt/sources.list  
RUN apt-get -y -q update && apt-get -y -q install megacli  
  
ENTRYPOINT [ "megacli" ]  

