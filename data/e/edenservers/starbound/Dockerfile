FROM phusion/baseimage:0.9.17  
MAINTAINER EdenServers  
  
#Ubuntu requirements  
WORKDIR /etc/apt/sources.list.d  
RUN echo "deb http://old-releases.ubuntu.com/ubuntu/ raring main restricted
universe multiverse" >ia32-libs-raring.list  
RUN dpkg --add-architecture i386  
RUN apt-get -y update  
RUN apt-get -y install ia32-libs  
RUN apt-get -y install wget  
  
#Steamcmd installation  
RUN mkdir -p /server/steamcmd  
RUN mkdir -p /server/starbound  
WORKDIR /server/steamcmd  
RUN wget http://media.steampowered.com/client/steamcmd_linux.tar.gz  
RUN tar -xvzf steamcmd_linux.tar.gz  
  
#Scp Server  
RUN apt-get install -y openssh-server rssh  
ADD rssh.conf /etc/rssh.conf  
  
#Server config  
EXPOSE 21025  
EXPOSE 21026  
#Server Start  
WORKDIR /server/starbound  
ADD start.sh /server/starbound/start.sh  
RUN chmod 755 /server/starbound/start.sh  
  
CMD ["/server/starbound/start.sh"]  

