FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN apt-get update && apt-get -y install lib32gcc1 lib32stdc++6 curl wget sudo
screen git vim zip unzip  
RUN apt-get clean  
RUN rm -rf /var/lib/apt  
  
# Run commands as the csgo user  
RUN useradd -m csgo && echo "csgo:csgo" | chpasswd && adduser csgo sudo  
USER csgo  
  
# Make folder for steamcmd  
RUN mkdir -p /home/csgo/steamcmd &&\  
cd /home/csgo/steamcmd &&\  
curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar
-vxz  
  
# Install CSGO dedicated server  
RUN mkdir /home/csgo/server &&\  
cd /home/csgo/steamcmd &&\  
./steamcmd.sh \  
+login anonymous \  
+force_install_dir /home/csgo/server \  
+app_update 740 \  
+quit  

