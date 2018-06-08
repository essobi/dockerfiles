FROM debian:7.11  
MAINTAINER mog54  
  
#Ubuntu requirements  
RUN dpkg --add-architecture i386  
RUN apt-get -y update  
RUN apt-get -y install ia32-libs  
RUN apt-get -y install curl wget file bzip2 gzip unzip bsdmainutils python
util-linux ca-certificates tmux lib32gcc1 libstdc++6 libstdc++6:i386  
  
#Steamcmd installation  
RUN mkdir -p /home/steamcmd &&\  
cd /home/steamcmd &&\  
wget http://media.steampowered.com/client/steamcmd_linux.tar.gz &&\  
tar -xvzf steamcmd_linux.tar.gz  
  
  
RUN apt-get install -y openssh-server rssh  
ADD rssh.conf /etc/rssh.conf  
  
#Server config  
EXPOSE 27015  
#Server Start  
ADD start.sh /home/steamcmd/start.sh  
RUN chmod 755 /home/steamcmd/start.sh  
  
CMD ["/home/steamcmd/start.sh"]  

