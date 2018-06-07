FROM phusion/baseimage:latest  
MAINTAINER Gunslinger  
  
#Ubuntu requirements  
WORKDIR /etc/apt/sources.list.d  
ADD sources.list.cn /etc/apt/sources.list.cn  
RUN mv /etc/apt/sources.list /etc/apt/sources.list.old  
RUN mv /etc/apt/sources.list.cn /etc/apt/sources.list  
RUN dpkg --add-architecture i386  
RUN apt-get -y update  
RUN apt-get -y install lib32gcc1  
RUN apt-get -y install curl  
RUN apt-get -y install screen  
  
#Steamcmd installation  
RUN mkdir -p /server/steamcmd  
RUN mkdir -p /server/csgo  
WORKDIR /server/steamcmd  
RUN curl -sqL
"https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar
zxvf -  
ADD update_csgo.txt /server/steamcmd/update_csgo.txt  
  
RUN apt-get install -y openssh-server rssh  
ADD rssh.conf /etc/rssh.conf  
  
#Server config  
EXPOSE 27015  
#Server Start  
WORKDIR /server/csgo  
ADD start.sh /server/csgo/start.sh  
RUN chmod 755 /server/csgo/start.sh  
  
CMD ["/server/csgo/start.sh"]  

